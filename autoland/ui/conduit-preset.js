const path = require('path');

const CopyPlugin = require('copy-webpack-plugin');
const lint = require('neutrino-lint-base');
const merge = require('deepmerge');


module.exports = neutrino => {
  // Ensure the path to JS and CSS starts from root
  neutrino.config.output.publicPath('/');

  // Ensure we have custom babel plugins
  neutrino.config.module
    .rule('compile')
    .loader('babel', ({ options }) => {
      options.plugins.unshift(require.resolve('babel-plugin-transform-class-properties'));
      return { options };
    });

  neutrino.config
    .plugin('copy')
    .use(CopyPlugin, [{ context: path.join(process.cwd(), 'assets'), from: `**/*` }]);

  // Implement custom linting
  lint(neutrino);
  neutrino.config.module
    .rule('lint')
    .loader('eslint', props => merge(props, {
      options: {
        globals: ['describe', 'expect', 'jest', 'test', 'document', 'window', 'fetch'],
        rules: {
          // Don't require () for single argument arrow functions
          'arrow-parens': 'off',
          // Don't require trailing commas
          'comma-dangle': 'off',
          // Don't require file extensions on imports
          'import/extensions': 'off',
          // Don't mark as unresolved without extensions
          'import/no-unresolved': 'off',
          // Don't let ESLint tell us how to use whitespace for imports
          'padded-blocks': 'off',
          // Hold off on propTypes for now
          'react/prop-types': 'off'
        },
        baseConfig: {
          extends: ['airbnb-base', 'plugin:react/recommended']
        }
      }
    }));
};
