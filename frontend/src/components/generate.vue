<!--
 * @Author: 秦少卫
 * @Date: 2022-09-03 19:16:55
 * @LastEditors: 秦少卫
 * @LastEditTime: 2022-09-06 23:20:40
 * @Description: 图层面板
-->

<template>
  <div class="generate">
    <h3>
      <button class="title-btn">
        <svg t="1690349229997" class="icon" viewBox="0 0 1152 1024" version="1.1" xmlns="http://www.w3.org/2000/svg"
          p-id="23556">
          <path
            d="M469.4 85.4L394 113.6c-6 2.2-10 8-10 14.4s4 12.2 10 14.4l75.4 28.2 28.2 75.4c2.2 6 8 10 14.4 10s12.2-4 14.4-10l28.2-75.4L630 142.4c6-2.2 10-8 10-14.4s-4-12.2-10-14.4l-75.4-28.2L526.4 10c-2.2-6-8-10-14.4-10s-12.2 4-14.4 10l-28.2 75.4zM92.2 790.8c-37.4 37.4-37.4 98.2 0 135.8l69.2 69.2c37.4 37.4 98.2 37.4 135.8 0l762.6-762.8c37.4-37.4 37.4-98.2 0-135.8l-69.2-69c-37.4-37.4-98.2-37.4-135.8 0L92.2 790.8zM969.2 165.2l-210 210-46.6-46.6 210-210 46.6 46.6zM15 234.4C6 237.8 0 246.4 0 256s6 18.2 15 21.6L128 320l42.4 113c3.4 9 12 15 21.6 15s18.2-6 21.6-15L256 320l113-42.4c9-3.4 15-12 15-21.6s-6-18.2-15-21.6L256 192l-42.4-113c-3.4-9-12-15-21.6-15s-18.2 6-21.6 15L128 192 15 234.4z m704 512c-9 3.4-15 12-15 21.6s6 18.2 15 21.6L832 832l42.4 113c3.4 9 12 15 21.6 15s18.2-6 21.6-15L960 832l113-42.4c9-3.4 15-12 15-21.6s-6-18.2-15-21.6L960 704l-42.4-113c-3.4-9-12-15-21.6-15s-18.2 6-21.6 15L832 704l-113 42.4z"
            p-id="23557"></path>
        </svg>
      </button>
      <span>GENERATE -------</span>
    </h3>


    <div class="img-input" style="display: flex; flex-direction: column; padding-left: 10px; ">

      <form>
        <textarea placeholder='Style, e.g, pixel art".' rows="2" id="generate-word" cols="21" class="generate-word"
          autocomplete="off" role="textbox" aria-autocomplete="list" aria-haspopup="true"></textarea>
      </form>


      <div class="generate-option" style="display: flex;">
        <button class="extract-feature-button">
          <img id="img-semantic" src="src\assets\generation\default\semantic.png">
        </button>
        <label for="semantic" class="custom-checkbox">
          <input type="checkbox" class="option-select-button" id="semantic">
          <span class="custom-button-semantic">
            <!-- <svg class="icon-option" viewBox="0 0 167 186" xmlns="http://www.w3.org/2000/svg">
              <path
                d="M165.75 100C167 98.75 167 96.25 167 93.75C167 91.25 167 88.75 165.75 87.5C164.5 85 162 83.75 160.75 82.5L18.25 1.25C14.5 -1.25 9.5 -1.25 5.75 1.25C3.25 2.5 3.25 3.75 2 6.25C0.750002 8.75 0.749998 10 0.749998 12.5V172.5C0.749998 175 0.750002 177.5 2 178.75C3.25 181.25 4.5 182.5 5.75 183.75C9.5 186.25 14.5 186.25 18.25 183.75L160.75 105C162 103.75 164.5 102.5 165.75 100Z" />
            </svg> -->
            <svg t="1690375449040" class="icon-option" viewBox="0 0 1024 1024" version="1.1"
              xmlns="http://www.w3.org/2000/svg" p-id="45210">
              <path
                d="M228.97664 141.85472A25.6 25.6 0 0 0 225.28 155.10528v713.79456a25.6 25.6 0 0 0 38.85056 21.90336l546.51392-330.60864c26.61376-16.1024 35.13856-50.72896 19.03616-77.34272a56.32 56.32 0 0 0-19.03616-19.03616L264.13056 133.20192a25.6 25.6 0 0 0-35.15392 8.6528zM174.08 868.89984V155.10528a76.8 76.8 0 0 1 11.08992-39.75168c21.95456-36.29056 69.1712-47.91296 105.46176-25.9584l546.51392 330.61376a107.52 107.52 0 0 1 36.34688 36.34176c30.73536 50.80576 14.464 116.9152-36.34688 147.65056l-546.5088 330.61376A76.8 76.8 0 0 1 250.88 945.69984c-42.41408 0-76.8-34.3808-76.8-76.8z"
                p-id="45211"></path>
            </svg>
          </span>
        </label>
      </div>

      <div class="generate-option" style="display: flex;">
        <button class="extract-feature-button">
          <img id="img-color" src="src\assets\generation\default\color.png">
        </button>
        <label for="color" class="custom-checkbox">
          <input type="checkbox" class="option-select-button" id="color">
          <span class="custom-button-color">
            <svg t="1690375449040" class="icon-option" viewBox="0 0 1024 1024" version="1.1"
              xmlns="http://www.w3.org/2000/svg" p-id="45210">
              <path
                d="M228.97664 141.85472A25.6 25.6 0 0 0 225.28 155.10528v713.79456a25.6 25.6 0 0 0 38.85056 21.90336l546.51392-330.60864c26.61376-16.1024 35.13856-50.72896 19.03616-77.34272a56.32 56.32 0 0 0-19.03616-19.03616L264.13056 133.20192a25.6 25.6 0 0 0-35.15392 8.6528zM174.08 868.89984V155.10528a76.8 76.8 0 0 1 11.08992-39.75168c21.95456-36.29056 69.1712-47.91296 105.46176-25.9584l546.51392 330.61376a107.52 107.52 0 0 1 36.34688 36.34176c30.73536 50.80576 14.464 116.9152-36.34688 147.65056l-546.5088 330.61376A76.8 76.8 0 0 1 250.88 945.69984c-42.41408 0-76.8-34.3808-76.8-76.8z"
                p-id="45211"></path>
            </svg>
          </span>
        </label>
      </div>

      <!-- <div class="generate-option" style="display: flex;">
        <button class="extract-feature-button">
          <img id="img-texture" src="src\assets\generation\default\texture.png">
        </button>
        <label for="texture" class="custom-checkbox">
          <input type="checkbox" class="option-select-button" id="texture">
          <span class="custom-button-texture">
            <svg t="1690375449040" class="icon-option" viewBox="0 0 1024 1024" version="1.1"
              xmlns="http://www.w3.org/2000/svg" p-id="45210">
              <path
                d="M228.97664 141.85472A25.6 25.6 0 0 0 225.28 155.10528v713.79456a25.6 25.6 0 0 0 38.85056 21.90336l546.51392-330.60864c26.61376-16.1024 35.13856-50.72896 19.03616-77.34272a56.32 56.32 0 0 0-19.03616-19.03616L264.13056 133.20192a25.6 25.6 0 0 0-35.15392 8.6528zM174.08 868.89984V155.10528a76.8 76.8 0 0 1 11.08992-39.75168c21.95456-36.29056 69.1712-47.91296 105.46176-25.9584l546.51392 330.61376a107.52 107.52 0 0 1 36.34688 36.34176c30.73536 50.80576 14.464 116.9152-36.34688 147.65056l-546.5088 330.61376A76.8 76.8 0 0 1 250.88 945.69984c-42.41408 0-76.8-34.3808-76.8-76.8z"
                p-id="45211"></path>
            </svg>
          </span>
        </label>
      </div> -->

      <div class="generate-option" style="display: flex;">
        <button class="extract-feature-button">
          <img id="img-shape" src="src\assets\generation\default\shape.png">
        </button>
        <label for="shape" class="custom-checkbox">
          <input type="checkbox" class="option-select-button" id="shape">
          <span class="custom-button-shape">
            <svg t="1690375449040" class="icon-option" viewBox="0 0 1024 1024" version="1.1"
              xmlns="http://www.w3.org/2000/svg" p-id="45210">
              <path
                d="M228.97664 141.85472A25.6 25.6 0 0 0 225.28 155.10528v713.79456a25.6 25.6 0 0 0 38.85056 21.90336l546.51392-330.60864c26.61376-16.1024 35.13856-50.72896 19.03616-77.34272a56.32 56.32 0 0 0-19.03616-19.03616L264.13056 133.20192a25.6 25.6 0 0 0-35.15392 8.6528zM174.08 868.89984V155.10528a76.8 76.8 0 0 1 11.08992-39.75168c21.95456-36.29056 69.1712-47.91296 105.46176-25.9584l546.51392 330.61376a107.52 107.52 0 0 1 36.34688 36.34176c30.73536 50.80576 14.464 116.9152-36.34688 147.65056l-546.5088 330.61376A76.8 76.8 0 0 1 250.88 945.69984c-42.41408 0-76.8-34.3808-76.8-76.8z"
                p-id="45211"></path>
            </svg>
          </span>
        </label>
      </div>

      <div class="slider-generate">
        <input type="range" id="control-generate" name="control-generate" min="0" max="1" value="0.75" step="0.01">
        <span class="range-slider__value" id="range-slider__value">0.75</span>
      </div>

    </div>

    <button class="generate-button" @click="clickGenerate">
      Generate
    </button>

  </div>
</template>

<script setup>
import { useI18n } from 'vue-i18n'
import { ref, toDisplayString } from 'vue';
import mitt from 'mitt';
import { useDesignPriorStore } from '../store/modules/imageViewStore'
import { useGenerateStore } from '../store/modules/generateStore';
import { startGenerate, startRetreiveInfo } from '../service/dataService';

const storeDesignPrior = useDesignPriorStore()
const storeGenerate = useGenerateStore()
const eventBus = inject("eventBus")
let labelImageList = ref([])
let generationStateDict = ref({})
let semanticPrompt = ref("")
let wrapSvg = ref([])

onMounted(() => {
  eventBus.on("isExtract", (data) => {
    console.log("come into generate view")
    const shapeImageUrl = storeDesignPrior.shapeImage;
    var imgShape = document.getElementById("img-shape");
    imgShape.src = shapeImageUrl

    const colorImageUrl = storeDesignPrior.colorImage;
    var imgShape = document.getElementById("img-color");
    imgShape.src = colorImageUrl

    const semanticImageUrl = storeDesignPrior.semanticImage;
    var imgShape = document.getElementById("img-semantic");
    imgShape.src = semanticImageUrl

    labelImageList.value = [semanticImageUrl, colorImageUrl, shapeImageUrl]
    semanticPrompt.value = storeDesignPrior.shapePrompt
  });

  eventBus.on("backTracking", (data) => {
    // 加载text
    const wordObject = document.querySelector(".generate-word")
    wordObject.value = storeGenerate.promptInfo
    // 加载option checked
    const semanticCheckbox = document.getElementById("semantic")
    semanticCheckbox.checked = storeGenerate.semanticLabel
    const colorCheckbox = document.getElementById("color")
    colorCheckbox.checked = storeGenerate.colorLabel
    const shapeCheckbox = document.getElementById("shape")
    shapeCheckbox.checked = storeGenerate.shapeLabel
    // 加载option 图片
    let labelImages = generationStateDict.value[storeGenerate.rowId]
    var imgShape = document.getElementById("img-shape");
    imgShape.src = labelImages[2]

    var imgShape = document.getElementById("img-color");
    imgShape.src = labelImages[1]

    var imgShape = document.getElementById("img-semantic");
    imgShape.src = labelImages[0]

  })

  // 一旦选择shape，后台要开始wrap
  const shapeCheckbox = document.getElementById("shape");
  shapeCheckbox.addEventListener('change', function () {
    if (this.checked) {

      // document.body.innerHTML += storeDesignPrior.svgString

      const textArea1 = document.getElementById("sample-points1");
      textArea1.value = storeDesignPrior.sampledPoints[0];
      const textArea2 = document.getElementById("sample-points2");
      textArea2.value = storeDesignPrior.sampledPoints[1];
      const textArea3 = document.getElementById("sample-points3");
      textArea3.value = storeDesignPrior.sampledPoints[2];
      const textArea4 = document.getElementById("sample-points4");
      textArea4.value = storeDesignPrior.sampledPoints[3];

      var img1 = document.getElementById("svg-wrapper1");
      var src1 = img1.getAttribute("src");
      img1.setAttribute("src", src1 + "?" + Date.now());
      var img2 = document.getElementById("svg-wrapper2");
      var src2 = img2.getAttribute("src");
      img2.setAttribute("src", src2 + "?" + Date.now());
      var img3 = document.getElementById("svg-wrapper3");
      var src3 = img3.getAttribute("src");
      img3.setAttribute("src", src3 + "?" + Date.now());
      var img4 = document.getElementById("svg-wrapper4");
      var src4 = img4.getAttribute("src");
      img4.setAttribute("src", src4 + "?" + Date.now());


      // 模拟点击wrap按钮
      const wrapButton1 = document.getElementById("wrap-button1")
      setTimeout(function () {
        wrapButton1.click()
      }, 1500);
      const wrapButton2 = document.getElementById("wrap-button2")
      setTimeout(function () {
        wrapButton2.click()
      }, 1500);
      const wrapButton3 = document.getElementById("wrap-button3")
      setTimeout(function () {
        wrapButton3.click()
      }, 1500);
      const wrapButton4 = document.getElementById("wrap-button4")
      setTimeout(function () {
        wrapButton4.click()
      }, 1500);


      // const textArea1 = document.getElementById("svg-point");
      // textArea1.value = storeDesignPrior.svgString;
    }
  });

  var slider = document.getElementById("control-generate");
  var rangeValue = document.getElementById("range-slider__value");

  slider.addEventListener("input", function () {
    rangeValue.textContent = slider.value;
  });
})

function clickGenerate() {
  // 获取text
  let inputTextarea = document.getElementById("generate-word").value;
  // 获取control strength 0-1
  let rangeValue = document.getElementById("range-slider__value");
  let strength = rangeValue.textContent;
  // 获取label
  let semanticOption = document.getElementById("semantic")
  const semanticOptionValue = semanticOption.checked
  let colorOption = document.getElementById("color")
  const colorOptionValue = colorOption.checked
  let shapeOption = document.getElementById("shape")
  const shapeOptionValue = shapeOption.checked
  // 获取wrap的svg结果（if shape在）
  if (shapeOptionValue) {
    const serializer = new XMLSerializer();
    const svgList= []
    const svg1 = document.getElementById('svg-wrapper1').getSVGDocument().getElementById('svg-element');
    const svg2 = document.getElementById('svg-wrapper2').getSVGDocument().getElementById('svg-element');
    const svg3 = document.getElementById('svg-wrapper3').getSVGDocument().getElementById('svg-element');
    const svg4 = document.getElementById('svg-wrapper4').getSVGDocument().getElementById('svg-element');
    svgList.push(serializer.serializeToString(svg1));
    svgList.push(serializer.serializeToString(svg2));
    svgList.push(serializer.serializeToString(svg3));
    svgList.push(serializer.serializeToString(svg4));
    wrapSvg.value = svgList;
  }
  else {
    wrapSvg.value = "";
  }
  // 生成stage1： 把info（text + image + label）显示出来
  let param = { "prompt": inputTextarea }
  let imageWordId = ""
  let imageImageId = ""
  startRetreiveInfo(param, function (data) {
    imageWordId = data.word.substr(data.word.indexOf(",") + 3600, 5)
    imageImageId = data.img.substr(data.img.indexOf(",") + 3600, 5) // 从逗号后面开始截取五个字
    // 生成stage2： 生成 gallery
    let uniqueStr = inputTextarea + semanticOptionValue.toString() + colorOptionValue.toString() + shapeOptionValue.toString() + imageWordId + imageImageId;
    // 属于是新的生成
    if (!(uniqueStr in generationStateDict.value)) {
      generationStateDict.value[uniqueStr] = labelImageList.value;
      let param = {
        "prompt": inputTextarea, "num_to_generate": 4,
        "strength": strength,
        "semantic_prompt": semanticPrompt.value,
        "generate-option": [semanticOptionValue, colorOptionValue, shapeOptionValue],
        "wrap_svg": wrapSvg.value,
        "previous_mode": [],
        "previous_img": []
      }
      startGenerate(param, function (data) {
        eventBus.emit("isGenerate", {
          "prompt": inputTextarea,
          "semanticOption": semanticOptionValue,
          "colorOption": colorOptionValue,
          "shapeOption": shapeOptionValue,
          "addRow": true,
          "imgList": data.gallery,
          "word": data.word,
          "image": data.img,
          "modeList": data.mode,
          "id": uniqueStr,
          "alt": data.alt,
        })
      })
    } else {
      let param = {
        "prompt": inputTextarea, "num_to_generate": storeGenerate.generateNum,
        "strength": strength,
        "semantic_prompt": semanticPrompt.value,
        "generate-option": [semanticOptionValue, colorOptionValue, shapeOptionValue],
        "wrap_svg": wrapSvg.value,
        "previous_mode": storeGenerate.rowModeList,
        "previous_img": storeGenerate.rowImageList,
      }
      console.log(storeGenerate.rowImageList);
      startGenerate(param, function (data) {
        eventBus.emit("isGenerate", {
          "prompt": inputTextarea,
          "semanticOption": semanticOptionValue,
          "colorOption": colorOptionValue,
          "shapeOption": shapeOptionValue,
          "addRow": false,
          "imgList": data.gallery,
          "word": data.word,
          "image": data.img,
          "modeList": data.mode,
          "id": uniqueStr,
          "alt": data.alt,
        })
      })
    }
  })
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="less">
.generate {
  width: 103%;
  height: 100%;
  margin-top: -30px;
  margin-left: 0px;
  margin-right: 5px;
  background: #fff;
}

h3 {
  margin-top: 30px;
  text-align: left;
  text-transform: uppercase;
  background: #fff;
  padding-top: 5px;
  padding-left: 10px;

  font-family: "DM Sans", sans-serif;
  color: #2a2a2a;
  font-size: 15px;
  font-weight: 600;
  margin-bottom: 10px;
}

.title-btn {
  background-color: #EDEFAB;
  border: none;
  border-radius: 5px;
  color: white;
  padding: 4px 4px;
  font-size: 18px;
  cursor: pointer;
  margin-right: 5px;
}

/* Darker background on mouse-over */
.title-btn.active {
  background-color: #EEF9FF;
  border: 15px;
  border-color: #a1a1a1;
}

.title-btn>.icon path {
  fill: #797B0B;
}

.extract-feature-button {
  padding: 0px;
  // margin-left: -10px;
  margin-right: 5px;
  margin-bottom: 1px;
  width: 126px;
  height: fit-content;
  border-radius: 10px;
  border: 0px;
  background-color: #fff;
}

.extract-feature-button img {
  border-radius: 3px;
  width: 126px;
  // margin-right: 32%;
}


.icon-option {
  // margin-top: -5px;
  width: 15px;
  height: 15px;
  // stroke: 3px;
}

.option-select-button {
  /* 隐藏checkbox的默认外观 */
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
  /* 设置自定义的外观 */
  display: inline-block;
  width: 35px;
  height: 35px;
  border: 1px solid #ccc;
  background-color: #fff;
  color: #333;
  text-align: center;
  line-height: 40px;
  cursor: pointer;
}

/* 设置选中时的样式 */
.option-select-button:checked {
  background-color: #007bff;
  color: #fff;
}

.custom-checkbox {
  /* 隐藏复选框的默认外观 */
  position: relative;
  display: inline-block;
}

.custom-checkbox input[type="checkbox"] {
  /* 隐藏复选框的默认外观 */
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
  /* 设置自定义的外观 */
  position: absolute;
  top: 0;
  left: 0;
  width: 35px;
  height: 35px;
  opacity: 0;
  cursor: pointer;
}

// semantic
.custom-checkbox .custom-button-semantic {
  /* 设置自定义按钮的样式 */
  display: inline-block;
  width: 33px;
  height: 33px;
  // border: 1px solid #ccc;
  background-color: #F7F6F0;
  color: #333;
  text-align: center;
  line-height: 40px;
  cursor: pointer;
  border-radius: 5px;
}

.custom-checkbox input[type="checkbox"]:checked+.custom-button-semantic {
  /* 设置选中时的样式 */
  background-color: #EDD896;
}

.custom-checkbox input[type="checkbox"]:checked+.custom-button-semantic>.icon-option path {
  /* 设置选中时的样式 */
  fill: #b99008;
}

.custom-button-semantic>.icon-option path {
  fill: #a0a0a0;
}

// color
.custom-checkbox .custom-button-color {
  /* 设置自定义按钮的样式 */
  display: inline-block;
  width: 33px;
  height: 33px;
  // border: 1px solid #ccc;
  background-color: #F7F6F0;
  color: #333;
  text-align: center;
  line-height: 40px;
  cursor: pointer;
  border-radius: 5px;
}

.custom-checkbox input[type="checkbox"]:checked+.custom-button-color {
  /* 设置选中时的样式 */
  background-color: #D0EAF6;
}

.custom-checkbox input[type="checkbox"]:checked+.custom-button-color>.icon-option path {
  /* 设置选中时的样式 */
  fill: #3c9ac6;
}

.custom-button-color>.icon-option path {
  fill: #a0a0a0;
}

// texture
.custom-checkbox .custom-button-texture {
  /* 设置自定义按钮的样式 */
  display: inline-block;
  width: 34px;
  height: 34px;
  // border: 1px solid #ccc;
  background-color: #F7F6F0;
  color: #333;
  text-align: center;
  line-height: 40px;
  cursor: pointer;
  border-radius: 5px;
}

.custom-checkbox input[type="checkbox"]:checked+.custom-button-texture {
  /* 设置选中时的样式 */
  background-color: #C1CDF7;
}

.custom-checkbox input[type="checkbox"]:checked+.custom-button-texture>.icon-option path {
  /* 设置选中时的样式 */
  fill: #4d67c4;
}

.custom-button-texture>.icon-option path {
  fill: #a0a0a0;
}

// shape
.custom-checkbox .custom-button-shape {
  /* 设置自定义按钮的样式 */
  display: inline-block;
  width: 33px;
  height: 33px;
  // border: 1px solid #ccc;
  background-color: #F7F6F0;
  color: #333;
  text-align: center;
  line-height: 40px;
  cursor: pointer;
  border-radius: 5px;
}

.custom-checkbox input[type="checkbox"]:checked+.custom-button-shape {
  /* 设置选中时的样式 */
  background-color: #C1CDF7;
}

.custom-checkbox input[type="checkbox"]:checked+.custom-button-shape>.icon-option path {
  /* 设置选中时的样式 */
  fill: #4d67c4;
}

.custom-button-shape>.icon-option path {
  fill: #a0a0a0;
}


.generate-button {
  width: 89%;
  height: 22px;
  background-color: #EDEFAB; //e1ecf4
  border-radius: 5px;
  border: 0px solid #EEF9FF; //#7aa7c7
  box-sizing: border-box;
  color: #797B0B;
  cursor: pointer;
  display: flex;
  align-items: center;
  /* 垂直居中 */
  justify-content: center;
  /* 水平居中 */
  font-family: -apple-system, system-ui, "Segoe UI", "Liberation Sans", sans-serif;
  font-size: 15px;
  font-weight: 560;
  line-height: 1.15385;
  outline: none;
  text-decoration: none;
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
  vertical-align: baseFIS;
  white-space: nowrap;
  margin-left: 10px;
  margin-right: 10px;
}

.generate-button:hover {
  background-color: #e3e699;
  color: #797B0B;
}

.generate-button:active {
  background-color: #e3e699;
  box-shadow: none;
  // color: #2c5777;
}

.generate-word {
  // margin-top: 10px;
  // margin-left: 2px;
  width: 148px;
  height: 20px;
  -moz-border-bottom-colors: none;
  -moz-border-left-colors: none;
  -moz-border-right-colors: none;
  -moz-border-top-colors: none;
  background: none repeat scroll 0 0 #F7F6F0;
  border-color: -moz-use-text-color #FFFFFF #FFFFFF -moz-use-text-color;
  border-image: none;
  border-radius: 6px 6px 6px 6px;
  // border-style: none solid solid none;
  border-style: none;
  // border-width: medium 1px 1px medium;
  // box-shadow: 0 1px 2px rgba(99, 99, 99, 0.12) inset;
  color: #4f4f4f;
  font-family: "DM Sans", sans-serif;
  font-size: 13px;
  line-height: 1.4em;
  padding: 5px 8px;
  transition: background-color 0.2s ease 0s;
  margin-top: -1px;
  margin-bottom: -1px;
}

.generate-word:focus {
  background: none repeat scroll 0 0 #f9f9f9;
  outline-width: 0;
}

/* Range slider */

.slider-generate {
  display: flex;
  width: 94%;
  align-items: center;
  justify-content: center;
  margin-bottom: 4px;
}

// 方法1 
// #control-generate {
//   // -webkit-appearance: none; /* 去除默认样式 */
//   width: 92%;
//   height: 5px;
//   background: #d2cdb0; /* 没有滑过的颜色 */
//   outline: none;
//   opacity: 0.7;
//   -webkit-transition: .2s;
//   transition: opacity .2s;
//   border-radius: 8px;
//   filter: hue-rotate(100deg); // 设置这个可以
//   // accent-color: #F55050; 设置这个可以
// }

// 方法2
@media screen and (-webkit-min-device-pixel-ratio:0) {
  input[type='range'] {
    overflow: hidden; // 非常关键
    width: 100%;
    height: 6px;
    -webkit-appearance: none;
    background-color: #F7F6F0;
    border-radius: 8px;
    // margin-bottom: 6px;
  }

  input[type='range']::-webkit-slider-thumb {
    -webkit-appearance: none;
    width: 10px;
    height: 10px;
    border-radius: 10px;
    cursor: pointer;
    background: #bab493; //797B0B
    box-shadow: -80px 0 0 80px #EDEFAB;
  }

}

// input[type='range']::before,
// input[type='range']::after {
//   content: attr(min);
//   position: absolute;
//   top: -10px;
//   color: #000;
// }

// input[type='range']::after {
//   content: attr(max);
//   top: -10px;
//   right: 0;
//   color: #000;
// }

.range-slider__value {
  display: inline-block;
  position: relative;
  width: 27%;
  color: #a0a0a0;
  font-size: 10px;
  line-height: 15px;
  text-align: center;
  border-radius: 3px;
  background: #F7F6F0;
  align-items: center;
  justify-content: center;
  // padding: 5px 5px;
  margin-left: 2px;
}
</style>