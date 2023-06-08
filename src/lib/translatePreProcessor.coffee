# translatePreProcessor.coffee

import MagicString from 'magic-string'

# ---------------------------------------------------------------------------

export translatePreProcessor = () =>

	return {
		markup: ({content, filename}) ->
			s = new MagicString(content)
			return {
				code: s.toString()
				map: s.generateMap({hires: true, file: filename})
				}
		}
