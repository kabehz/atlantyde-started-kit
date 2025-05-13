
// @ts-check
// Note: type annotations allow type checking and IDEs autocompletion

const config = {
  title: 'Atl0s Docs',
  tagline: 'Documentación Semántica Gamificada',
  url: 'https://your-site.com',
  baseUrl: '/',
  onBrokenLinks: 'throw',
  favicon: 'img/favicon.ico',
  organizationName: 'atlos', // Usually your GitHub org/user name.
  projectName: 'starter-kit', // Usually your repo name.

  presets: [
    [
      'classic',
      ({
        docs: {
          path: 'docs',
          routeBasePath: '/',
          sidebarPath: require.resolve('./sidebars.js'),
          editUrl: 'https://github.com/atlos/starter-kit/edit/main/',
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      }),
    ],
  ],

  themeConfig: {
    navbar: {
      title: 'Atl0s Kit',
      items: [
        {
          type: 'doc',
          docId: 'semantic-map',
          position: 'left',
          label: 'Mapa Semántico',
        },
        {
          href: 'https://github.com/atlos/starter-kit',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
  },
};

module.exports = config;
