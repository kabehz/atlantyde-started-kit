import React from 'react';
import banner from '/public/visual/docusaurus.svg';

export default function DocusaurusBanner() {
  return <img src={banner} alt="docusaurus banner" className="w-full max-w-xl mx-auto rounded-md shadow-md" />;
}
