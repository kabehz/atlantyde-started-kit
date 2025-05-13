# atlci.py - CLI para gestión de Makefile desde Python
import subprocess
import argparse

COMMANDS = [
    "validate", "deploy", "local", "setup", "deploy-workflows", "github-ci", "clean-workflows", "test", "help"
]

def run_make(target):
    if target == "github-ci":
        run_opa_checks()
        run_codeql_scan()
    subprocess.run(["make", target], check=True)

def run_opa_checks():
    print("🔒 Ejecutando políticas OPA...")
    subprocess.run(["opa", "eval", "data.policies.allow == true", "--data", "./ci/policies", "--format", "pretty"], check=True)

def run_codeql_scan():
    print("🧪 Ejecutando análisis CodeQL...")
    subprocess.run(["codeql", "database", "create", "codeql-db", "--language=python", "--command=python3 -m compileall ."], check=True)
    subprocess.run(["codeql", "analyze", "codeql-db", "--format=sarifv2", "--output=results.sarif"], check=True)

def main():
    parser = argparse.ArgumentParser(description="CLI para ejecutar comandos Makefile de AtlantydeKit")
    parser.add_argument("target", choices=COMMANDS, help="Tarea make a ejecutar")
    args = parser.parse_args()
    run_make(args.target)

if __name__ == "__main__":
    main()
