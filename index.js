require('dotenv').config()
const { start } = require('./controllers/runner.controller')

start()
  .then(() => console.log('✅ Execução finalizada'))
  .catch(err => console.error('❌ Erro geral:', err))