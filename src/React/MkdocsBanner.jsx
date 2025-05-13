import React from 'react';
import banner from '/public/visual/mkdocs.svg';

export default function MkdocsBanner() {
  return <img src={banner} alt="mkdocs banner" className="w-full max-w-xl mx-auto rounded-md shadow-md" />;
}
