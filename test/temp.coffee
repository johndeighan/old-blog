# temp.coffee

import {scaleLinear} from 'd3-scale'

console.log "Hello, World!"

xScale = scaleLinear().domain([0, 15]).range([0, 100])

result = xScale(5)
console.log "scaled = #{result}"
