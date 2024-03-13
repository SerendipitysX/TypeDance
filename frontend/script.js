function warp1() {
  console.log("wrap begin!!!")
  // var path_data = font.getPath(text, 0, 100, 100).toSVG(3),

  var svg_c = document.getElementById('svg-control'),
    controlPath = document.getElementById('control-path');

  // var img = document.getElementById("svg-wrapper");
  // var src = img.getAttribute("src");
  // img.setAttribute("src", src + "?" + Date.now());

  var svg = document.getElementById('svg-wrapper1').getSVGDocument().getElementById('svg-element');

  var path = svg.querySelector("path"),
    path_box = path.getBBox(),
    path_x = 0,
    path_y = 0,
    path_w = svg.width.baseVal.value,
    path_h = svg.height.baseVal.value,

    // 初始化
    controlPoints = [ // 注意方向 17
      [path_x, path_y],
      [path_x, path_y + path_h * 0.25],
      [path_x, path_y + path_h * 0.5],
      [path_x, path_y + path_h * 0.75],
      [path_x, path_y + path_h],
      [path_x + path_w * 0.25, path_y + path_h],
      [path_x + path_w * 0.5, path_y + path_h],
      [path_x + path_w * 0.75, path_y + path_h],
      [path_x + path_w, path_y + path_h],
      [path_x + path_w, path_y + path_h * 0.75],
      [path_x + path_w, path_y + path_h * 0.5],
      [path_x + path_w, path_y + path_h * 0.25],
      [path_x + path_w, path_y],
      [path_x + path_w * 0.75, path_y],
      [path_x + path_w * 0.5, path_y],
      [path_x + path_w * 0.25, path_y],
      [path_x + path_w * 0.12, path_y],
    ];
  const controlBuffer = 0.1;

  var warp = new Warp(svg);
  warp.interpolate(2); // sets the number of interpolated points between each pair of control points.

  for (var i = 0; i < controlPoints.length; i++) {
    if (controlPoints[i][0] === 0) controlPoints[i][0] -= controlBuffer;
    if (controlPoints[i][1] === 0) controlPoints[i][1] -= controlBuffer;
    if (controlPoints[i][0] === path_w) controlPoints[i][0] += controlBuffer;
    if (controlPoints[i][1] === path_h) controlPoints[i][1] += controlBuffer;
  }

  //
  // Compute weights from control points

  warp.transform(function (v0) {
    var V = arguments.length <= 1 || arguments[1] === undefined ? controlPoints : arguments[1];

    var A = [];
    var W = [];
    var L = [];

    // Find angles
    for (var i = 0; i < V.length; i++) {
      var j = (i + 1) % V.length; // 当 i 达到 V.length - 1 时，j 将会是 0，从而实现了循环。

      var vi = V[i];
      var vj = V[j]; // 相邻的两个点

      var r0i = Math.sqrt(Math.pow(v0[0] - vi[0], 2) + Math.pow(v0[1] - vi[1], 2)); // dist(v0, vi)
      var r0j = Math.sqrt(Math.pow(v0[0] - vj[0], 2) + Math.pow(v0[1] - vj[1], 2)); // dist(v0,, vj)
      var rij = Math.sqrt(Math.pow(vi[0] - vj[0], 2) + Math.pow(vi[1] - vj[1], 2)); // dist(vi, vj)

      var dn = 2 * r0i * r0j;
      var r = (Math.pow(r0i, 2) + Math.pow(r0j, 2) - Math.pow(rij, 2)) / dn; // 余弦定理， 得到当前夹角的余弦值

      A[i] = isNaN(r) ? 0 : Math.acos(Math.max(-1, Math.min(r, 1))); // 得到夹角大小
    }

    // Find weights
    for (var j = 0; j < V.length; j++) {
      var i = (j > 0 ? j : V.length) - 1; // 保证vi是vj的上一个

      var vi = V[i];
      var vj = V[j];

      var r = Math.sqrt(Math.pow(vj[0] - v0[0], 2) + Math.pow(vj[1] - v0[1], 2));

      W[j] = (Math.tan(A[i] / 2) + Math.tan(A[j] / 2)) / r;
    }

    // Normalise weights
    var Ws = W.reduce(function (a, b) {
      return a + b;
    }, 0); // 求和
    for (var i = 0; i < V.length; i++) {
      L[i] = W[i] / Ws;
    }

    // Save weights to the point for use when transforming
    return [].concat(v0, L);
  });

  // Warp function
  // 通过使用均值坐标，我们可以根据控制点的位置和权重来调整点的位置，从而产生平滑的变形效果。
  function reposition(_ref2) {
    console.log("start repositioning")
    var W = _ref2.slice(2);

    var V = arguments.length <= 1 || arguments[1] === undefined ? controlPoints : arguments[1];
    // var V = storeDesignPrior.sampledPoints;

    var nx = 0;
    var ny = 0;

    // Recreate the points using mean value coordinates
    for (var i = 0; i < V.length; i++) {
      nx += W[i] * V[i][0];
      ny += W[i] * V[i][1];
    }

    return [nx, ny].concat(W);
  }

  const pointValue = document.getElementById("sample-points1").value;
  // console.log(pointValue)
  // console.log(pointValue.value)

  let arr = JSON.parse(pointValue);
  let result = Array.from(arr);
  console.log(result)
  var controlPoints = result;// 注意方向
  console.log(controlPoints);
  // var controlPoints = [
  //   [80, 297],
  //   [140, 353],
  //   [223, 372],
  //   [190, 396],
  //   [250, 485],
  //   [281, 474],
  //   [293, 421],
  //   [354, 436],
  //   [371, 316],
  //   [428, 248],
  //   [431, 201],
  //   [328, 30],
  //   [299, 99],
  //   [240, 26],
  //   [94, 99],
  //   [132, 163],
  //   [83, 217],
  // ];

  warp.transform(reposition);

  const textArea = document.getElementById("sample-points1");
  textArea.value = "";
  // textArea1.value = "";

}

function warp2() {
  console.log("wrap begin!!!")
  // var path_data = font.getPath(text, 0, 100, 100).toSVG(3),

  var svg_c = document.getElementById('svg-control'),
    controlPath = document.getElementById('control-path');

  // var img = document.getElementById("svg-wrapper");
  // var src = img.getAttribute("src");
  // img.setAttribute("src", src + "?" + Date.now());

  var svg = document.getElementById('svg-wrapper2').getSVGDocument().getElementById('svg-element');

  var path = svg.querySelector("path"),
    path_box = path.getBBox(),
    path_x = 0,
    path_y = 0,
    path_w = svg.width.baseVal.value,
    path_h = svg.height.baseVal.value,

    // 初始化
    controlPoints = [ // 注意方向 17
      [path_x, path_y],
      [path_x, path_y + path_h * 0.25],
      [path_x, path_y + path_h * 0.5],
      [path_x, path_y + path_h * 0.75],
      [path_x, path_y + path_h],
      [path_x + path_w * 0.25, path_y + path_h],
      [path_x + path_w * 0.5, path_y + path_h],
      [path_x + path_w * 0.75, path_y + path_h],
      [path_x + path_w, path_y + path_h],
      [path_x + path_w, path_y + path_h * 0.75],
      [path_x + path_w, path_y + path_h * 0.5],
      [path_x + path_w, path_y + path_h * 0.25],
      [path_x + path_w, path_y],
      [path_x + path_w * 0.75, path_y],
      [path_x + path_w * 0.5, path_y],
      [path_x + path_w * 0.25, path_y],
      [path_x + path_w * 0.12, path_y],
    ];
  const controlBuffer = 0.1;

  var warp = new Warp(svg);
  warp.interpolate(2); // sets the number of interpolated points between each pair of control points.

  for (var i = 0; i < controlPoints.length; i++) {
    if (controlPoints[i][0] === 0) controlPoints[i][0] -= controlBuffer;
    if (controlPoints[i][1] === 0) controlPoints[i][1] -= controlBuffer;
    if (controlPoints[i][0] === path_w) controlPoints[i][0] += controlBuffer;
    if (controlPoints[i][1] === path_h) controlPoints[i][1] += controlBuffer;
  }

  //
  // Compute weights from control points

  warp.transform(function (v0) {
    var V = arguments.length <= 1 || arguments[1] === undefined ? controlPoints : arguments[1];

    var A = [];
    var W = [];
    var L = [];

    // Find angles
    for (var i = 0; i < V.length; i++) {
      var j = (i + 1) % V.length; // 当 i 达到 V.length - 1 时，j 将会是 0，从而实现了循环。

      var vi = V[i];
      var vj = V[j]; // 相邻的两个点

      var r0i = Math.sqrt(Math.pow(v0[0] - vi[0], 2) + Math.pow(v0[1] - vi[1], 2)); // dist(v0, vi)
      var r0j = Math.sqrt(Math.pow(v0[0] - vj[0], 2) + Math.pow(v0[1] - vj[1], 2)); // dist(v0,, vj)
      var rij = Math.sqrt(Math.pow(vi[0] - vj[0], 2) + Math.pow(vi[1] - vj[1], 2)); // dist(vi, vj)

      var dn = 2 * r0i * r0j;
      var r = (Math.pow(r0i, 2) + Math.pow(r0j, 2) - Math.pow(rij, 2)) / dn; // 余弦定理， 得到当前夹角的余弦值

      A[i] = isNaN(r) ? 0 : Math.acos(Math.max(-1, Math.min(r, 1))); // 得到夹角大小
    }

    // Find weights
    for (var j = 0; j < V.length; j++) {
      var i = (j > 0 ? j : V.length) - 1; // 保证vi是vj的上一个

      var vi = V[i];
      var vj = V[j];

      var r = Math.sqrt(Math.pow(vj[0] - v0[0], 2) + Math.pow(vj[1] - v0[1], 2));

      W[j] = (Math.tan(A[i] / 2) + Math.tan(A[j] / 2)) / r;
    }

    // Normalise weights
    var Ws = W.reduce(function (a, b) {
      return a + b;
    }, 0); // 求和
    for (var i = 0; i < V.length; i++) {
      L[i] = W[i] / Ws;
    }

    // Save weights to the point for use when transforming
    return [].concat(v0, L);
  });

  // Warp function
  // 通过使用均值坐标，我们可以根据控制点的位置和权重来调整点的位置，从而产生平滑的变形效果。
  function reposition(_ref2) {
    console.log("start repositioning")
    var W = _ref2.slice(2);

    var V = arguments.length <= 1 || arguments[1] === undefined ? controlPoints : arguments[1];
    // var V = storeDesignPrior.sampledPoints;

    var nx = 0;
    var ny = 0;

    // Recreate the points using mean value coordinates
    for (var i = 0; i < V.length; i++) {
      nx += W[i] * V[i][0];
      ny += W[i] * V[i][1];
    }

    return [nx, ny].concat(W);
  }

  const pointValue = document.getElementById("sample-points2").value;
  // console.log(pointValue)
  // console.log(pointValue.value)

  let arr = JSON.parse(pointValue);
  let result = Array.from(arr);
  console.log(result)
  var controlPoints = result;// 注意方向
  console.log(controlPoints);
  // var controlPoints = [
  //   [80, 297],
  //   [140, 353],
  //   [223, 372],
  //   [190, 396],
  //   [250, 485],
  //   [281, 474],
  //   [293, 421],
  //   [354, 436],
  //   [371, 316],
  //   [428, 248],
  //   [431, 201],
  //   [328, 30],
  //   [299, 99],
  //   [240, 26],
  //   [94, 99],
  //   [132, 163],
  //   [83, 217],
  // ];

  warp.transform(reposition);

  const textArea = document.getElementById("sample-points2");
  textArea.value = "";
  // textArea1.value = "";

}

function warp3() {
  console.log("wrap begin!!!")
  // var path_data = font.getPath(text, 0, 100, 100).toSVG(3),

  var svg_c = document.getElementById('svg-control'),
    controlPath = document.getElementById('control-path');

  // var img = document.getElementById("svg-wrapper");
  // var src = img.getAttribute("src");
  // img.setAttribute("src", src + "?" + Date.now());

  var svg = document.getElementById('svg-wrapper3').getSVGDocument().getElementById('svg-element');

  var path = svg.querySelector("path"),
    path_box = path.getBBox(),
    path_x = 0,
    path_y = 0,
    path_w = svg.width.baseVal.value,
    path_h = svg.height.baseVal.value,

    // 初始化
    controlPoints = [ // 注意方向 17
      [path_x, path_y],
      [path_x, path_y + path_h * 0.25],
      [path_x, path_y + path_h * 0.5],
      [path_x, path_y + path_h * 0.75],
      [path_x, path_y + path_h],
      [path_x + path_w * 0.25, path_y + path_h],
      [path_x + path_w * 0.5, path_y + path_h],
      [path_x + path_w * 0.75, path_y + path_h],
      [path_x + path_w, path_y + path_h],
      [path_x + path_w, path_y + path_h * 0.75],
      [path_x + path_w, path_y + path_h * 0.5],
      [path_x + path_w, path_y + path_h * 0.25],
      [path_x + path_w, path_y],
      [path_x + path_w * 0.75, path_y],
      [path_x + path_w * 0.5, path_y],
      [path_x + path_w * 0.25, path_y],
      [path_x + path_w * 0.12, path_y],
    ];
  const controlBuffer = 0.1;

  var warp = new Warp(svg);
  warp.interpolate(2); // sets the number of interpolated points between each pair of control points.

  for (var i = 0; i < controlPoints.length; i++) {
    if (controlPoints[i][0] === 0) controlPoints[i][0] -= controlBuffer;
    if (controlPoints[i][1] === 0) controlPoints[i][1] -= controlBuffer;
    if (controlPoints[i][0] === path_w) controlPoints[i][0] += controlBuffer;
    if (controlPoints[i][1] === path_h) controlPoints[i][1] += controlBuffer;
  }

  //
  // Compute weights from control points

  warp.transform(function (v0) {
    var V = arguments.length <= 1 || arguments[1] === undefined ? controlPoints : arguments[1];

    var A = [];
    var W = [];
    var L = [];

    // Find angles
    for (var i = 0; i < V.length; i++) {
      var j = (i + 1) % V.length; // 当 i 达到 V.length - 1 时，j 将会是 0，从而实现了循环。

      var vi = V[i];
      var vj = V[j]; // 相邻的两个点

      var r0i = Math.sqrt(Math.pow(v0[0] - vi[0], 2) + Math.pow(v0[1] - vi[1], 2)); // dist(v0, vi)
      var r0j = Math.sqrt(Math.pow(v0[0] - vj[0], 2) + Math.pow(v0[1] - vj[1], 2)); // dist(v0,, vj)
      var rij = Math.sqrt(Math.pow(vi[0] - vj[0], 2) + Math.pow(vi[1] - vj[1], 2)); // dist(vi, vj)

      var dn = 2 * r0i * r0j;
      var r = (Math.pow(r0i, 2) + Math.pow(r0j, 2) - Math.pow(rij, 2)) / dn; // 余弦定理， 得到当前夹角的余弦值

      A[i] = isNaN(r) ? 0 : Math.acos(Math.max(-1, Math.min(r, 1))); // 得到夹角大小
    }

    // Find weights
    for (var j = 0; j < V.length; j++) {
      var i = (j > 0 ? j : V.length) - 1; // 保证vi是vj的上一个

      var vi = V[i];
      var vj = V[j];

      var r = Math.sqrt(Math.pow(vj[0] - v0[0], 2) + Math.pow(vj[1] - v0[1], 2));

      W[j] = (Math.tan(A[i] / 2) + Math.tan(A[j] / 2)) / r;
    }

    // Normalise weights
    var Ws = W.reduce(function (a, b) {
      return a + b;
    }, 0); // 求和
    for (var i = 0; i < V.length; i++) {
      L[i] = W[i] / Ws;
    }

    // Save weights to the point for use when transforming
    return [].concat(v0, L);
  });

  // Warp function
  // 通过使用均值坐标，我们可以根据控制点的位置和权重来调整点的位置，从而产生平滑的变形效果。
  function reposition(_ref2) {
    console.log("start repositioning")
    var W = _ref2.slice(2);

    var V = arguments.length <= 1 || arguments[1] === undefined ? controlPoints : arguments[1];
    // var V = storeDesignPrior.sampledPoints;

    var nx = 0;
    var ny = 0;

    // Recreate the points using mean value coordinates
    for (var i = 0; i < V.length; i++) {
      nx += W[i] * V[i][0];
      ny += W[i] * V[i][1];
    }

    return [nx, ny].concat(W);
  }

  const pointValue = document.getElementById("sample-points3").value;
  // console.log(pointValue)
  // console.log(pointValue.value)

  let arr = JSON.parse(pointValue);
  let result = Array.from(arr);
  console.log(result)
  var controlPoints = result;// 注意方向
  console.log(controlPoints);
  // var controlPoints = [
  //   [80, 297],
  //   [140, 353],
  //   [223, 372],
  //   [190, 396],
  //   [250, 485],
  //   [281, 474],
  //   [293, 421],
  //   [354, 436],
  //   [371, 316],
  //   [428, 248],
  //   [431, 201],
  //   [328, 30],
  //   [299, 99],
  //   [240, 26],
  //   [94, 99],
  //   [132, 163],
  //   [83, 217],
  // ];

  warp.transform(reposition);

  const textArea = document.getElementById("sample-points3");
  textArea.value = "";
  // textArea1.value = "";

}

function warp4() {
  console.log("wrap begin!!!")
  // var path_data = font.getPath(text, 0, 100, 100).toSVG(3),

  var svg_c = document.getElementById('svg-control'),
    controlPath = document.getElementById('control-path');

  // var img = document.getElementById("svg-wrapper");
  // var src = img.getAttribute("src");
  // img.setAttribute("src", src + "?" + Date.now());

  var svg = document.getElementById('svg-wrapper4').getSVGDocument().getElementById('svg-element');

  var path = svg.querySelector("path"),
    path_box = path.getBBox(),
    path_x = 0,
    path_y = 0,
    path_w = svg.width.baseVal.value,
    path_h = svg.height.baseVal.value,

    // 初始化
    controlPoints = [ // 注意方向 17
      [path_x, path_y],
      [path_x, path_y + path_h * 0.25],
      [path_x, path_y + path_h * 0.5],
      [path_x, path_y + path_h * 0.75],
      [path_x, path_y + path_h],
      [path_x + path_w * 0.25, path_y + path_h],
      [path_x + path_w * 0.5, path_y + path_h],
      [path_x + path_w * 0.75, path_y + path_h],
      [path_x + path_w, path_y + path_h],
      [path_x + path_w, path_y + path_h * 0.75],
      [path_x + path_w, path_y + path_h * 0.5],
      [path_x + path_w, path_y + path_h * 0.25],
      [path_x + path_w, path_y],
      [path_x + path_w * 0.75, path_y],
      [path_x + path_w * 0.5, path_y],
      [path_x + path_w * 0.25, path_y],
      [path_x + path_w * 0.12, path_y],
    ];
  const controlBuffer = 0.1;

  var warp = new Warp(svg);
  warp.interpolate(2); // sets the number of interpolated points between each pair of control points.

  for (var i = 0; i < controlPoints.length; i++) {
    if (controlPoints[i][0] === 0) controlPoints[i][0] -= controlBuffer;
    if (controlPoints[i][1] === 0) controlPoints[i][1] -= controlBuffer;
    if (controlPoints[i][0] === path_w) controlPoints[i][0] += controlBuffer;
    if (controlPoints[i][1] === path_h) controlPoints[i][1] += controlBuffer;
  }

  //
  // Compute weights from control points

  warp.transform(function (v0) {
    var V = arguments.length <= 1 || arguments[1] === undefined ? controlPoints : arguments[1];

    var A = [];
    var W = [];
    var L = [];

    // Find angles
    for (var i = 0; i < V.length; i++) {
      var j = (i + 1) % V.length; // 当 i 达到 V.length - 1 时，j 将会是 0，从而实现了循环。

      var vi = V[i];
      var vj = V[j]; // 相邻的两个点

      var r0i = Math.sqrt(Math.pow(v0[0] - vi[0], 2) + Math.pow(v0[1] - vi[1], 2)); // dist(v0, vi)
      var r0j = Math.sqrt(Math.pow(v0[0] - vj[0], 2) + Math.pow(v0[1] - vj[1], 2)); // dist(v0,, vj)
      var rij = Math.sqrt(Math.pow(vi[0] - vj[0], 2) + Math.pow(vi[1] - vj[1], 2)); // dist(vi, vj)

      var dn = 2 * r0i * r0j;
      var r = (Math.pow(r0i, 2) + Math.pow(r0j, 2) - Math.pow(rij, 2)) / dn; // 余弦定理， 得到当前夹角的余弦值

      A[i] = isNaN(r) ? 0 : Math.acos(Math.max(-1, Math.min(r, 1))); // 得到夹角大小
    }

    // Find weights
    for (var j = 0; j < V.length; j++) {
      var i = (j > 0 ? j : V.length) - 1; // 保证vi是vj的上一个

      var vi = V[i];
      var vj = V[j];

      var r = Math.sqrt(Math.pow(vj[0] - v0[0], 2) + Math.pow(vj[1] - v0[1], 2));

      W[j] = (Math.tan(A[i] / 2) + Math.tan(A[j] / 2)) / r;
    }

    // Normalise weights
    var Ws = W.reduce(function (a, b) {
      return a + b;
    }, 0); // 求和
    for (var i = 0; i < V.length; i++) {
      L[i] = W[i] / Ws;
    }

    // Save weights to the point for use when transforming
    return [].concat(v0, L);
  });

  // Warp function
  // 通过使用均值坐标，我们可以根据控制点的位置和权重来调整点的位置，从而产生平滑的变形效果。
  function reposition(_ref2) {
    console.log("start repositioning")
    var W = _ref2.slice(2);

    var V = arguments.length <= 1 || arguments[1] === undefined ? controlPoints : arguments[1];
    // var V = storeDesignPrior.sampledPoints;

    var nx = 0;
    var ny = 0;

    // Recreate the points using mean value coordinates
    for (var i = 0; i < V.length; i++) {
      nx += W[i] * V[i][0];
      ny += W[i] * V[i][1];
    }

    return [nx, ny].concat(W);
  }

  const pointValue = document.getElementById("sample-points4").value;
  // console.log(pointValue)
  // console.log(pointValue.value)

  let arr = JSON.parse(pointValue);
  let result = Array.from(arr);
  console.log(result)
  var controlPoints = result;// 注意方向
  console.log(controlPoints);
  // var controlPoints = [
  //   [80, 297],
  //   [140, 353],
  //   [223, 372],
  //   [190, 396],
  //   [250, 485],
  //   [281, 474],
  //   [293, 421],
  //   [354, 436],
  //   [371, 316],
  //   [428, 248],
  //   [431, 201],
  //   [328, 30],
  //   [299, 99],
  //   [240, 26],
  //   [94, 99],
  //   [132, 163],
  //   [83, 217],
  // ];

  warp.transform(reposition);

  const textArea = document.getElementById("sample-points4");
  textArea.value = "";
  // textArea1.value = "";

}