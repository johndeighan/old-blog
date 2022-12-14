// Generated by CoffeeScript 2.7.0
  // GraphLib.coffee
import {
  scaleLinear
} from 'd3-scale';

import {
  undef,
  defined
} from '@jdeighan/base-utils';

// ---------------------------------------------------------------------------
export var adjustedData = (lRawData, xField, yField, idField, adjField = undef) => {
  var h, lPoints, x, xmax, xmin, y, ymax, ymin;
  // --- Returns {lPoints, xRange, yRange}
  xmin = ymin = Number.MAX_VALUE;
  xmax = ymax = Number.MIN_VALUE;
  lPoints = (function() {
    var i, len, results;
    results = [];
    for (i = 0, len = lRawData.length; i < len; i++) {
      h = lRawData[i];
      x = h[xField];
      if (defined(adjField)) {
        x /= h[adjField];
      }
      if (x < xmin) {
        xmin = x;
      } else if (x > xmax) {
        xmax = x;
      }
      y = h[yField];
      if (defined(adjField)) {
        y /= h[adjField];
      }
      if (y < ymin) {
        ymin = y;
      } else if (y > ymax) {
        ymax = y;
      }
      results.push({
        x,
        y,
        id: h[idField]
      });
    }
    return results;
  })();
  return {
    lPoints,
    xRange: {
      min: xmin,
      max: xmax
    },
    yRange: {
      min: ymin,
      max: ymax
    }
  };
};

// ---------------------------------------------------------------------------
export var getScale = (map1, map2) => {
  var maxG, maxV, minG, minV;
  [minV, minG] = map1;
  [maxV, maxG] = map2;
  return scaleLinear().domain([minV, maxV]).range([minG, maxG]);
};
