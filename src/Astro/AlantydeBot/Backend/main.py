from fastapi import FastAPI, HTTPException, BackgroundTasks
from pydantic import BaseModel, EmailStr
from uuid import uuid4
import subprocess
import os

app = FastAPI()

class KeyRequest(BaseModel):
    name: str
    email: EmailStr
    expiration: str = "2y"

KEY_DIR = "/tmp/gpg-keys"
os.makedirs(KEY_DIR, exist_ok=True)

@app.post("/generate")
def generate_key(req: KeyRequest, background_tasks: BackgroundTasks):
    key_id = str(uuid4())
    key_dir = os.path.join(KEY_DIR, key_id)
    os.makedirs(key_dir)
    config_path = os.path.join(key_dir, "gpg-key.conf")
    with open(config_path, "w") as f:
        f.write(f"""
        %echo Generating a GPG key
        Key-Type: eddsa
        Key-Curve: ed25519
        Key-Usage: sign
        Subkey-Type: ecdh
        Subkey-Curve: cv25519
        Subkey-Usage: encrypt
        Name-Real: {req.name}
        Name-Email: {req.email}
        Expire-Date: {req.expiration}
        %no-protection
        %commit
        %echo done
        """)
    background_tasks.add_task(run_gpg_batch, config_path, key_dir)
    return {"status": "processing", "key_id": key_id}

def run_gpg_batch(config_path: str, key_dir: str):
    env = os.environ.copy()
    env['GNUPGHOME'] = key_dir
    subprocess.run(["gpg", "--batch", "--generate-key", config_path], env=env, check=True)
    with open(os.path.join(key_dir, "public.asc"), "w") as pub:
        subprocess.run(["gpg", "--armor", "--export"], env=env, stdout=pub, check=True)
    with open(os.path.join(key_dir, "private.asc"), "w") as priv:
        subprocess.run(["gpg", "--armor", "--export-secret-keys"], env=env, stdout=priv, check=True)

@app.get("/status/{key_id}")
def check_status(key_id: str):
    key_dir = os.path.join(KEY_DIR, key_id)
    pub_path = os.path.join(key_dir, "public.asc")
    if os.path.exists(pub_path):
        return {"status": "ready", "public_key": f"/download/{key_id}/public.asc"}
    return {"status": "pending"}

@app.get("/download/{key_id}/{filename}")
def download_key(key_id: str, filename: str):
    file_path = os.path.join(KEY_DIR, key_id, filename)
    if os.path.exists(file_path):
        return open(file_path, "rb").read()
    raise HTTPException(status_code=404, detail="Archivo no encontrado")
