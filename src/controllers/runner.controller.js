const SpreadsheetRepo = require('../repositories/spreadsheet.repository')
const NeoService = require('../services/neoservice.service')
const AppMissService = require('../services/appmiss.service')
const Report = require('../services/report.service')

async function start() {
  const rows = SpreadsheetRepo.read()

  for (const row of rows) {
    try {
      const code = await NeoService.execute(row)
      await AppMissService.execute(row, code)

      Report.success(row)
    } catch (err) {
      Report.error(row, err)
    }
  }

  Report.finish()
}

module.exports = { start }
