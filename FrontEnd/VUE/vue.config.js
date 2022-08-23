const {defineConfig} = require('@vue/cli-service')

module.exports = defineConfig({
  transpileDependencies: true,
  pwa: {
    name: 'Photos Retouch',
    shortName: 'Photos Retouch',
    themeColor: '#3DEEF7',
    msTileColor: '#000000'
  }
})