import React from 'react';
import banner from '/public/visual/astro.svg';

export default function AstroBanner() {
  return <img src={banner} alt="astro banner" className="w-full max-w-xl mx-auto rounded-md shadow-md" />;
}
