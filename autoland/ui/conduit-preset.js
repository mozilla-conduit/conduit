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
};
