<!--
 * @Author: 秦少卫
 * @Date: 2022-09-03 19:16:55
 * @LastEditors: 秦少卫
 * @LastEditTime: 2022-09-06 23:20:40
 * @Description: 图层面板
-->

<template>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

  <div class="ideaView">
    <h3>
      <button class="title-btn">
        <svg t="1690124817154" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg"
          p-id="11543">
          <path
            d="M511.788986 108.889278a32.666783 32.666783 0 0 0 32.666784-32.666783v-43.555712a32.666783 32.666783 0 0 0-65.333567 0v43.555712a32.666783 32.666783 0 0 0 32.666783 32.666783zM969.123955 413.997036h-43.555711a32.666783 32.666783 0 0 0 0 65.333567h43.555711a32.666783 32.666783 0 0 0 0-65.333567zM130.676512 446.66382A32.797451 32.797451 0 0 0 98.009729 413.997036h-43.555711a32.666783 32.666783 0 0 0 0 65.333567h43.555711A32.666783 32.666783 0 0 0 130.676512 446.66382z m768.758305 258.938704a28.986326 28.986326 0 0 0-41.63926 0 29.922774 29.922774 0 0 0 0 42.031261l27.788544 28.093434a29.574328 29.574328 0 0 0 41.63926-42.031262zM130.676512 692.753589l-30.815665 31.142333a33.407231 33.407231 0 0 0 0 46.82239 32.666783 32.666783 0 0 0 46.190831 0l30.815666-31.142334a33.145896 33.145896 0 0 0 0-46.604611 32.29656 32.29656 0 0 0-46.081942-0.217778z m696.891382-170.085053A308.025991 308.025991 0 0 0 517.516563 217.560778 297.529064 297.529064 0 0 0 217.657268 518.748522a304.084199 304.084199 0 0 0 155.472111 273.747646 39.875254 39.875254 0 0 0-3.157789 28.311212v67.729131c0 74.698045 52.114409 135.458262 125.396893 135.458262h44.296159A134.325814 134.325814 0 0 0 675.122904 893.109861v-65.333567a64.985121 64.985121 0 0 0-10.475149-35.280126A305.325536 305.325536 0 0 0 827.567894 522.668536zM609.789337 827.776294v21.777855h-114.35552a32.666783 32.666783 0 1 0 0 65.333567h110.348395a70.974032 70.974032 0 0 1-66.052237 43.77349h-44.296158c-36.695687 0-59.82377-32.666783-59.82377-70.124695v-67.729131l81.754071 6.968914H609.789337z m-91.989662-65.333567h-0.435557A238.685298 238.685298 0 0 1 283.121502 518.748522a231.651051 231.651051 0 0 1 234.438616-235.636398A239.687079 239.687079 0 1 1 517.734341 762.442727z m-0.217779-424.885964a32.666783 32.666783 0 1 0 0 65.333567 120.997766 120.997766 0 0 1 121.803547 119.778206 33.233008 33.233008 0 0 0 66.444237 0 186.875779 186.875779 0 0 0-188.313117-185.111773z m382.027144 368.045761a28.986326 28.986326 0 0 0-41.63926 0 29.922774 29.922774 0 0 0 0 42.031261l27.788544 28.093434a29.574328 29.574328 0 0 0 41.63926-42.031262z m-768.758305-12.848935l-30.815666 31.142333a33.407231 33.407231 0 0 0 0 46.82239 32.666783 32.666783 0 0 0 46.190832 0l30.815666-31.142334a33.145896 33.145896 0 0 0 0-46.604611 32.29656 32.29656 0 0 0-46.256165-0.217778zM823.081655 122.827106l-32.165892 32.884562a35.323682 35.323682 0 0 0 0 49.217954 33.51612 33.51612 0 0 0 48.216172 0l32.144115-32.884562a35.280126 35.280126 0 0 0 0-49.217954 33.537898 33.537898 0 0 0-48.259728 0z m-651.157884-2.831121l34.844569 34.844569a36.913465 36.913465 0 1 1-52.114409 52.266853l-34.844569-34.844569A36.957021 36.957021 0 0 1 172.054438 119.995985z"
            p-id="11544"></path>
        </svg>
      </button>
      <span>IDEATION ---------------------</span>
    </h3>

    <div class="idea-input" style="display: flex; align-items: center; padding-left: 10px; ">
      <form>
        <textarea placeholder="Describe the concept" rows="20" name="idea" id="idea" cols="40" class="text-idea"
          autocomplete="off" role="textbox" aria-autocomplete="list" aria-haspopup="true"></textarea>
      </form>
      <button class="button-idea" @click="clickBrainstorm">Brain
        storm</button>
    </div>
    <ul class="tags" style="padding-left: 10px;">
      <el-tooltip effect="light" placement="top-start" :content="ttipContent1">
        <li>
          <a href="#" class="tag" id="tag-concept1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</a>
        </li>
      </el-tooltip>

      <el-tooltip effect="light" placement="top-start" :content="ttipContent2">
        <li>
          <a href="#" class="tag" id="tag-concept2">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</a>
        </li>
      </el-tooltip>

      <el-tooltip effect="light" placement="top-start" :content="ttipContent3">
        <li>
          <a href="#" class="tag" id="tag-concept3">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</a>
        </li>
      </el-tooltip>

      <el-tooltip effect="light" placement="top-start" :content="ttipContent4">
        <li>
          <a href="#" class="tag" id="tag-concept4">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</a>
        </li>
      </el-tooltip>

      <el-tooltip effect="light" placement="top-start" :content="ttipContent5">
        <li>
          <a href="#" class="tag" id="tag-concept5">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</a>
        </li>
      </el-tooltip>


    </ul>

  </div>

  <div class="wordView">
    <h3>
      <button class="title-btn">
        <svg t="1690097700978" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg"
          p-id="6347">
          <path
            d="M853.333333 1024 170.666667 1024c-93.866667 0-170.666667-76.8-170.666667-170.666667L0 170.666667c0-93.866667 76.8-170.666667 170.666667-170.666667l682.666667 0c93.866667 0 170.666667 76.8 170.666667 170.666667l0 682.666667C1024 947.2 947.2 1024 853.333333 1024zM170.666667 85.333333C123.733333 85.333333 85.333333 123.733333 85.333333 170.666667l0 682.666667c0 46.933333 38.4 85.333333 85.333333 85.333333l682.666667 0c46.933333 0 85.333333-38.4 85.333333-85.333333L938.666667 170.666667c0-46.933333-38.4-85.333333-85.333333-85.333333L170.666667 85.333333z"
            p-id="6348">
          </path>
          <path
            d="M725.333333 341.333333 298.666667 341.333333C273.066667 341.333333 256 324.266667 256 298.666667s17.066667-42.666667 42.666667-42.666667l426.666667 0c25.6 0 42.666667 17.066667 42.666667 42.666667S750.933333 341.333333 725.333333 341.333333z"
            p-id="6349"></path>
          <path
            d="M298.666667 384C273.066667 384 256 366.933333 256 341.333333L256 298.666667c0-25.6 17.066667-42.666667 42.666667-42.666667s42.666667 17.066667 42.666667 42.666667l0 42.666667C341.333333 366.933333 324.266667 384 298.666667 384z"
            p-id="6350"></path>
          <path
            d="M725.333333 384c-25.6 0-42.666667-17.066667-42.666667-42.666667L682.666667 298.666667c0-25.6 17.066667-42.666667 42.666667-42.666667s42.666667 17.066667 42.666667 42.666667l0 42.666667C768 366.933333 750.933333 384 725.333333 384z"
            p-id="6351"></path>
          <path
            d="M512 768c-25.6 0-42.666667-17.066667-42.666667-42.666667L469.333333 298.666667c0-25.6 17.066667-42.666667 42.666667-42.666667s42.666667 17.066667 42.666667 42.666667l0 426.666667C554.666667 750.933333 537.6 768 512 768z"
            p-id="6352"></path>
          <path
            d="M554.666667 768l-85.333333 0c-25.6 0-42.666667-17.066667-42.666667-42.666667s17.066667-42.666667 42.666667-42.666667l85.333333 0c25.6 0 42.666667 17.066667 42.666667 42.666667S580.266667 768 554.666667 768z"
            p-id="6353">
          </path>
        </svg>
        <!-- <svg t="1690097451111" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="5328">
          <path d="M640 512a128 128 0 1 0 0-256 128 128 0 0 0 0 256z m0-64a64 64 0 1 0 0-128 64 64 0 0 0 0 128z" p-id="5329">
          </path>
          <path d="M128 832a64 64 0 0 0 64 64h640a64 64 0 0 0 64-64V192a64 64 0 0 0-64-64H192a64 64 0 0 0-64 64v640z m64-82.752l192-192L658.752 832H192v-82.752z m0-90.496V192h640v640h-82.752L384 466.752l-192 192z" p-id="5330">
        </path></svg> -->
      </button>
      <span>Typeface ---------------------</span>
    </h3>

    <div class="word-input" style="display: inline-block; padding-left: 10px; ">
      <form>
        <textarea placeholder="Input the word" rows="20" name="object" id="object" cols="40" class="text-word"
          autocomplete="off" role="textbox" aria-autocomplete="list" aria-haspopup="true"></textarea>
      </form>
      <div class="word-options">
        <!-- <button class="inline-button" @click="changeFont">Font Type ▼</button> -->
        <el-select class="inline-button" placeholder="Font type" style="width: 39%;" v-model="selectedFont">
          <el-option v-for="item in fontFamilyList" :value="item" :key="'font-' + item">{{ item }}</el-option>
        </el-select>
        <button class="inline-button" @click="displayText">Display</button>
        <button class="inline-button" id="addButton" @click="addSelectionTrigger" style="width: fit-content;">
          <svg t="1694243217565" class="icon-function" style="width: 12px;" viewBox="0 0 1024 1024" version="1.1"
            xmlns="http://www.w3.org/2000/svg" p-id="9676">
            <path d="M992 464H560V32h-96v432H32v96h432v432h96V560h432z" p-id="9677"></path>
          </svg>
        </button>
        <button class="inline-button" id="confirmButton" @click="displayTextOnCanvas" style="width: 42px;">
          <svg t="1690350488185" class="icon-function" viewBox="0 0 1024 1024" version="1.1"
            xmlns="http://www.w3.org/2000/svg" p-id="37475">
            <path
              d="M346.595344 684.495656 135.774825 473.675136l-71.492264 71.447239 282.312784 282.268782 606.406137-606.358041-71.447239-71.492264L346.595344 684.495656z"
              p-id="37476"></path>
          </svg>
        </button>
      </div>

      <canvas id="canva-word" width="232" height="150"></canvas>
    </div>
  </div>

  <div class="imageView">
    <h3>
      <button class="title-btn">
        <svg t="1690097881001" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg"
          p-id="7490">
          <path d="M416 266.538667m-96 0a96 96 0 1 0 192 0 96 96 0 1 0-192 0Z" p-id="7491"></path>
          <path
            d="M721.749333 371.626667A43.818667 43.818667 0 0 0 682.666667 348.074667a42.965333 42.965333 0 0 0-38.058667 25.002666l-66.474667 146.517334a10.624 10.624 0 0 1-18.005333 2.261333l-34.986667-43.690667a42.666667 42.666667 0 0 0-34.688-16.042666 42.965333 42.965333 0 0 0-33.578666 18.176L323.84 670.293333a21.333333 21.333333 0 0 0 17.493333 33.706667h512a21.333333 21.333333 0 0 0 18.133334-10.112 21.333333 21.333333 0 0 0 0.938666-20.736z"
            p-id="7492"></path>
          <path
            d="M938.666667 0H234.666667a85.333333 85.333333 0 0 0-85.333334 85.333333v704a85.333333 85.333333 0 0 0 85.333334 85.333334H938.666667a85.333333 85.333333 0 0 0 85.333333-85.333334V85.333333a85.333333 85.333333 0 0 0-85.333333-85.333333z m-6.186667 783.104a21.333333 21.333333 0 0 1-15.104 6.229333H256a21.333333 21.333333 0 0 1-21.333333-21.333333V106.666667A21.333333 21.333333 0 0 1 256 85.333333h661.333333a21.333333 21.333333 0 0 1 21.333334 21.333334V768a21.333333 21.333333 0 0 1-6.186667 14.976z"
            p-id="7493"></path>
          <path
            d="M832 938.666667h-725.333333a21.333333 21.333333 0 0 1-21.333334-21.333334v-725.333333a42.666667 42.666667 0 0 0-85.333333 0V938.666667a85.333333 85.333333 0 0 0 85.333333 85.333333h746.666667a42.666667 42.666667 0 0 0 0-85.333333z"
            p-id="7494"></path>
        </svg>
      </button>
      <span>IMAGERY ---------------------</span>
    </h3>

    <div class="img-input" style="display: flex; align-items: center; padding-left: 10px; ">
      <div class="upload-img-container" style="display: flex; flex-direction: column; padding-left: 10px;">
        <button class="upload-img" @click="loadImageOrDisplay1">
          <img id="img1" width="50" height="50" src="src\assets\upload_image\default1.png">
          <input id="input-img1" type="file" name="contact_image_1" />
        </button>
        <button class="upload-img" @click="loadImageOrDisplay2">
          <img id="img2" width="50" height="50" src="src\assets\upload_image\default1.png"></button>
        <input id="input-img2" type="file" name="contact_image_1" />
        <button class="upload-img" @click="loadImageOrDisplay3">
          <img id="img3" width="50" height="50" src="src\assets\upload_image\default1.png"></button>
        <input id="input-img3" type="file" name="contact_image_1" />
        <!-- <div class="img-button-container" style="display: flex; justify-content: space-between; margin-right: 5px;"> -->
        <!-- <button class="lassoButton-img" id="lassoButton-img">
          <svg t="1690350605083" class="icon-function-small" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="42621" >
            <path d="M351.866914 645.910768c-43.577233 0-85.884838-8.547496-125.723167-25.39256-38.458733-16.265235-72.998614-39.548414-102.63993-69.199727-29.651313-29.651313-52.924495-64.181197-69.199726-102.63993-16.855062-39.838329-25.392561-82.145934-25.392561-125.723167s8.547496-85.884838 25.392561-125.723167c16.265235-38.458733 39.548414-72.998614 69.199726-102.63993 29.651313-29.651313 64.181197-52.924495 102.63993-69.199726C265.982076 8.537499 308.289681 0 351.866914 0s85.884838 8.547496 125.723167 25.392561c38.458733 16.265235 72.998614 39.548414 102.63993 69.199726 29.651313 29.651313 52.924495 64.181197 69.199726 102.63993 16.855062 39.838329 25.392561 82.145934 25.392561 125.723167 0 21.883589-2.209353 43.767178-6.558079 65.040945l-77.647251-15.885346c3.289036-16.055296 4.94855-32.600449 4.94855-49.155599 0-134.380631-109.32797-243.708601-243.708601-243.708601S108.158313 188.574753 108.158313 322.955384 217.486283 566.663985 351.866914 566.663985c16.495167 0 32.980338-1.649517 48.985649-4.918559l15.83536 77.657249c-21.213785 4.318735-43.017397 6.508093-64.821009 6.508093z" fill="#333333" p-id="42622"></path><path d="M904.345055 563.674861L533.173797 893.248306 371.491165 337.351167zM725.547437 722.428351L966.186937 997.607732" fill="#333333" p-id="42623"></path><path d="M695.754166 748.540701l59.66452-52.174714 240.643499 275.187378-59.66452 52.174715z" p-id="42624"></path>
          </svg>
        </button> -->
        <button class="lassoButton-img" id="lassoButton-img" @click="startExtract">
          <svg t="1690350488185" class="icon-function-small" viewBox="0 0 1024 1024" version="1.1"
            xmlns="http://www.w3.org/2000/svg" p-id="37475">
            <path
              d="M346.595344 684.495656 135.774825 473.675136l-71.492264 71.447239 282.312784 282.268782 606.406137-606.358041-71.447239-71.492264L346.595344 684.495656z"
              p-id="37476"></path>
          </svg>
        </button>
        <!-- </div> -->
      </div>
      <canvas id="canva-img" width="180" height="180"></canvas>
    </div>
  </div>
</template>

<script setup>
import { ref, provide } from 'vue';
import { useRouter, useRoute } from 'vue-router'
import { useSettingStore, useJsonStore } from '../store/modules/settingStore'
import { useDesignPriorStore } from '../store/modules/imageViewStore'
import { startBrainStorm, imageSegment, startImageExtract } from '../service/dataService';
import fontList from "@/assets/fonts/font";
import { fabric } from 'fabric';

const canvas = inject("canvas")
const storeDesignPrior = useDesignPriorStore()
const eventBus = inject("eventBus")

// // =================== ABOUT FONT ==========================
// let fontFamilyList = ref(fontList.map(item => item.fontFamily))
// let selectedFont = ref("Arial")
// let finalX = ref(0)
// let finalY = ref(0)
// let finalHeight = ref(0)
// let finalFontSize = ref(100)
// let finalText = ref("fighting")
// let firstDisplayWord = ref(true)

// function displayText() {
//   var textarea = document.getElementById("object");
//   var canvas = document.getElementById("canva-word");
//   var ctx = canvas.getContext("2d");
//   // console.log(canvas.width, canvas.height)
//   // Clear the canvas
//   ctx.clearRect(0, 0, canvas.width, canvas.height);

//   // Set the maximum font size and position
//   var maxFontSize = 120;
//   if (firstDisplayWord.value) {
//     var x = canvas.width / 2;
//     var y = canvas.height / 2;
//   }
//   else {
//     var x = canvas.width / 4;
//     var y = canvas.height / 4;
//   }

//   // Get the text from the textarea
//   var text = textarea.value;

//   // Set the initial font size
//   var fontSize = maxFontSize;

//   // Decrease the font size until the text fits within the canvas
//   do {
//     // Set the font and text color
//     ctx.font = fontSize + "px Times New Roman";
//     ctx.fillStyle = "black";

//     // Measure the width of the text
//     var textWidth = ctx.measureText(text).width;

//     // Decrease the font size
//     fontSize--;

//     // Break the loop if the font size becomes too small
//     if (fontSize <= 0) {
//       break;
//     }
//   } while (textWidth > canvas.width);
//   ctx.font = fontSize + "px Times New Roman";
//   ctx.fillStyle = "black";
//   let textHeight = ctx.measureText(text).actualBoundingBoxAscent;
//   // Set the final font size and position
//   ctx.font = fontSize + "px " + selectedFont.value;
//   x -= textWidth / 2;
//   y += textHeight / 2 - 10;
//   finalX.value = x
//   finalY.value = y
//   finalHeight.value = textHeight
//   finalFontSize.value = fontSize
//   finalText.value = text

//   // Display the text on the canvas
//   ctx.fillText(text, x, y);
// }

// // =================== ABOUT LASSO ==========================
// // getElementById 只能在点击之后使用，因为我这个是setup模式，这些东西都还没加载呢
// const isLassoEnabled = ref(false) // 开关
// function startLasso() {
//   isLassoEnabled.value = !isLassoEnabled.value;
//   // delete canvas
//   if (isLassoEnabled.value) {
//     var oldCanvas = document.getElementById("canva-word");
//     if (firstDisplayWord.value) {
//       oldCanvas.parentNode.removeChild(oldCanvas);
//       firstDisplayWord.value = false
//     }
//     else {
//       var parentElement = oldCanvas.parentNode;
//       var grandparentElement = parentElement.parentNode;
//       grandparentElement.removeChild(parentElement);
//     }
//     // create canvas
//     const wordInputDiv = document.querySelector(".word-input");
//     const canvasWord0 = document.createElement("canvas")

//     canvasWord0.id = "canva-word";
//     canvasWord0.width = 232;
//     canvasWord0.height = 150;
//     wordInputDiv.appendChild(canvasWord0);
//     // add style for canvas
//     const style = document.createElement("style");
//     style.innerHTML = `
//     .canvas-container {
//       background-color: #ffffff;
//       padding: 5px 8px;
//       border-radius: 6px;
//       border: 1px solid #cacaca; }`;
//     document.head.appendChild(style);

//     // add fabric
//     const canvasWord = new fabric.Canvas('canva-word', { isDrawingMode: true });

//     // card.set('backgroundColor', 'red');
//     canvasWord.setWidth(232);
//     canvasWord.setHeight(150);
//     canvasWord.renderAll()
//     // console.log(canvasWord)
//     console.log(finalHeight.value)
//     var text = new fabric.Text(finalText.value, {
//       left: finalX.value,
//       top: finalY.value - finalHeight.value - 10,
//       fontSize: finalFontSize.value,
//       fill: 'black',
//       fontFamily: selectedFont.value,
//     });
//     canvasWord.add(text);
//     canvasWord.controlsAboveOverlay = true;
//     canvasWord.freeDrawingBrush.color = "#797B0B"
//     canvasWord.freeDrawingBrush.width = 1

//     canvasWord.on('mouse:wheel', opt => {
//       let delta = opt.e.deltaY // 滚轮，向上滚一下是 -100，向下滚一下是 100
//       let zoom = canvasWord.getZoom() // 获取画布当前缩放值
//       zoom *= 0.999 ** delta
//       if (zoom > 5) zoom = 5
//       if (zoom < 0.5) zoom = 0.5
//       canvasWord.zoomToPoint({ // 关键点
//         x: opt.e.offsetX,
//         y: opt.e.offsetY
//       },
//         zoom
//       )
//       opt.e.preventDefault()
//       opt.e.stopPropagation()
//     })

//     canvasWord.on('path:created', function (options) {
//       console.log("start drawing")
//       var path = options.path;
//       path.set('fill', 'black');
//       console.log(path)
//       canvasWord.isDrawingMode = false;
//       canvasWord.remove(path);
//       canvasWord.clipPath = path;
//     });
//   } else {
//   }
// }

// =================== ABOUT FONT ==========================
let fontFamilyList = ref(fontList.map(item => item.fontFamily))
let selectedFont = ref("Arial")
let firstDisplayWord = ref(true)
let addSelection = ref(false)
let select_boxes = ref([])
let current_box = ref([])

function displayText() {
  var textarea = document.getElementById("object");
  // delete old canvas
  var oldCanvas = document.getElementById("canva-word");

  if (firstDisplayWord.value) {
    oldCanvas.parentNode.removeChild(oldCanvas);
    firstDisplayWord.value = false
  }
  else {
    var parentElement = oldCanvas.parentNode;
    var grandparentElement = parentElement.parentNode;
    grandparentElement.removeChild(parentElement);

    // clear cache
    addSelection.value = false;
    select_boxes.value = []
  }

  // add new canvas
  const imgInputDiv = document.querySelector(".word-input");
  const canvasWord0 = document.createElement("canvas")

  canvasWord0.id = "canva-word";
  canvasWord0.width = 232;
  canvasWord0.height = 150;
  imgInputDiv.appendChild(canvasWord0);

  // add style for canvas
  const style = document.createElement("style");
  style.innerHTML = `
  .canvas-container {
    background-color: #ffffff;
    padding: 5px 8px;
    border-radius: 6px;
    border: 1px solid #cacaca; }`;
  document.head.appendChild(style);

  const canvasWord = new fabric.Canvas('canva-word', { backgroundColor: "white" });
  // canvasWord.setWidth(232);
  // canvasWord.setHeight(150);
  canvasWord.renderAll()

  var ctx = canvasWord.getContext("2d");
  // Clear the canvas
  ctx.clearRect(0, 0, 232, 150);

  // Set the maximum font size and position
  var maxFontSize = 130;
  var x = 232 / 2;
  var y = 150 / 2;

  // Get the text from the textarea
  var text = textarea.value;

  // Set the initial font size
  var fontSize = maxFontSize;

  // Decrease the font size until the text fits within the canvas
  do {
    // Set the font and text color
    ctx.font = fontSize + "px Times New Roman";
    ctx.fillStyle = "black";

    // Measure the width of the text
    var textWidth = ctx.measureText(text).width + 25;
    // Decrease the font size
    fontSize--;

    // Break the loop if the font size becomes too small
    if (fontSize <= 0) {
      break;
    }
  } while (textWidth > canvasWord.width);
  ctx.font = fontSize + "px Times New Roman";
  ctx.fillStyle = "black";
  let textHeight = ctx.measureText(text).actualBoundingBoxAscent;
  // Set the final font size and position
  ctx.font = fontSize + "px " + selectedFont.value;
  x -= (textWidth / 2);
  y -= ((textHeight / 2) + 10);

  // Display the text on the canvas
  // ctx.fillText(text, x, y);
  const textInstance = new fabric.IText(text, {
    left: x,
    top: y,
    fontSize: fontSize,
    fill: 'black',
    fontFamily: selectedFont.value,
  });
  textInstance.selectable = false;
  canvasWord.add(textInstance);

  // free draw rectangle
  var rectangle, isDown, origX, origY;

  canvasWord.on('mouse:down', function (o) {
    var pointer = canvasWord.getPointer(o.e);

    isDown = true;
    origX = pointer.x;
    origY = pointer.y;

    rectangle = new fabric.Rect({
      left: origX,
      top: origY,
      fill: 'transparent',
      // stroke: '#6cffd6',
      // stroke: '#797B0B',
      strokeWidth: 0,
    });
    rectangle.selectable = false
    canvasWord.add(rectangle);
  });

  canvasWord.on('mouse:move', function (o) {
    if (!isDown) return;
    var pointer = canvasWord.getPointer(o.e);
    if (origX > pointer.x) {
      rectangle.set({ left: Math.abs(pointer.x) });
    }
    if (origY > pointer.y) {
      rectangle.set({ top: Math.abs(pointer.y) });
    }

    rectangle.set({ width: Math.abs(origX - pointer.x) });
    rectangle.set({ height: Math.abs(origY - pointer.y) });
    canvasWord.renderAll();
  });

  // 这个就是信号
  canvasWord.on('mouse:up', function (o) {
    isDown = false;
    const option = { format: 'png', quality: 2, multiplier: 2 }
    const dataUrl = canvasWord.toDataURL(option)
    current_box.value = [rectangle.left * 2, rectangle.top * 2, (rectangle.left + rectangle.width) * 2, (rectangle.top + rectangle.height) * 2];
    if (addSelection.value == true) {
      console.log(select_boxes.value);
      select_boxes.value.push(current_box.value);
      let param = {
        "box": select_boxes.value,
        "image_url": dataUrl,
        "mode": "word"
      };
      imageSegment(param, function (data) {
        const imgEl = document.createElement('img');
        imgEl.src = data
        // 插入页面
        document.body.appendChild(imgEl);
        imgEl.onload = () => { // 必须要加onload，等图片加载完全，不然就是空的
          canvasWord.clear();
          const imgInstanceNew = new fabric.Image(imgEl, {
            left: 0, top: 0,
          });
          // 设置缩放
          imgInstanceNew.scaleToWidth(canvasWord.getWidth());
          imgInstanceNew.scaleToHeight(canvasWord.getHeight());
          imgInstanceNew.selectable = false;

          canvasWord.add(imgInstanceNew)
          canvasWord.renderAll()
          // 删除页面中的图片元素
          imgEl.remove()
        }

        canvasWord.renderAll()
      })
    }
    else {
      let param = {
        "box": current_box.value,
        "image_url": dataUrl,
        "mode": "word"
      };
      console.log(current_box.value);
      imageSegment(param, function (data) {
        const imgEl = document.createElement('img');
        imgEl.src = data
        // 插入页面
        document.body.appendChild(imgEl);
        imgEl.onload = () => { // 必须要加onload，等图片加载完全，不然就是空的
          canvasWord.clear();
          const imgInstanceNew = new fabric.Image(imgEl, {
            left: 0, top: 0,
          });
          // 设置缩放
          imgInstanceNew.scaleToWidth(canvasWord.getWidth());
          imgInstanceNew.scaleToHeight(canvasWord.getHeight());
          imgInstanceNew.selectable = false;

          canvasWord.add(imgInstanceNew)
          canvasWord.renderAll()
          // 删除页面中的图片元素
          imgEl.remove()
        }

        canvasWord.renderAll()
      })
    }

  });


}

function addSelectionTrigger() {
  addSelection.value = true;
  select_boxes.value.push(current_box.value);
}

function displayTextOnCanvas() {
  fabric.loadSVGFromURL('/src/assets/canvas/word.svg', function (objects, options) {
    var svgObject = fabric.util.groupSVGElements(objects, options);
    svgObject.id = "word";
    canvas.c.add(svgObject);
  });
}

// =================== ABOUT IDEA ===========================
let ttipContent1 = ref("explanation")
let ttipContent2 = ref("explanation")
let ttipContent3 = ref("explanation")
let ttipContent4 = ref("explanation")
let ttipContent5 = ref("explanation")
function clickBrainstorm() {
  const textareaIdea = document.getElementById("idea");
  console.log("press storm")
  let param = {
    "user_prompt": textareaIdea.value
  };

  startBrainStorm(param, function (data) {
    var count = 1

    for (let key in data) {
      let concept = key;
      let explanation = data[key];
      const labelConcept = document.getElementById("tag-concept" + String(count)); const tooltipConcept = document.getElementById("item-concept" + String(count));
      labelConcept.textContent = concept;
      if (count == 1) {
        ttipContent1.value = explanation
      }
      if (count == 2) {
        ttipContent2.value = explanation
      }
      if (count == 3) {
        ttipContent3.value = explanation
      }
      if (count == 4) {
        ttipContent4.value = explanation
      }
      if (count == 5) {
        ttipContent5.value = explanation
      }
      count++;
    }
  });
}

// =================== ABOUT IMAGE ==========================
let isExistCanvasImage = ref(false)
let firstDisplay = ref(true)
// // box
// function loadImageOrDisplay1() {
//   var img1 = document.getElementById("img1");
//   // 初始上传，点击上传本地文件
//   if (img1.src == "http://localhost/src/assets/upload_image/default1.png") {
//     document.getElementById('input-img1').click()
//     document.getElementById('input-img1').addEventListener('change', function (event) {
//       var file = event.target.files[0];
//       var reader = new FileReader();
//       reader.onload = function (event) {
//         img1.src = event.target.result;
//       };
//       reader.readAsDataURL(file);
//     });
//   }
//   // 已经上传好了，点击显示到canvas上
//   else {
//     // 删掉原有的canvas再新建一个，再加入fabric canvas
//     // fabric canvas 有两个，原先的这个canvas只是第一个，共同归属canvas-container管
//     var oldCanvas = document.getElementById("canva-img");
//     if (firstDisplay.value) {
//       oldCanvas.parentNode.removeChild(oldCanvas);
//       firstDisplay.value = false
//     }
//     else {
//       var parentElement = oldCanvas.parentNode;
//       var grandparentElement = parentElement.parentNode;
//       grandparentElement.removeChild(parentElement);
//     }

//     // add new canvas
//     const imgInputDiv = document.querySelector(".img-input");
//     const canvasImage0 = document.createElement("canvas")

//     canvasImage0.id = "canva-img";
//     canvasImage0.width = 180;
//     canvasImage0.height = 180;
//     imgInputDiv.appendChild(canvasImage0);

//     // add style for canvas
//     const style = document.createElement("style");
//     style.innerHTML = `
//     .canvas-container {
//       background-color: #ffffff;
//       padding: 5px 8px;
//       border-radius: 6px;
//       border: 1px solid #cacaca; }`;
//     document.head.appendChild(style);

//     // add image instance 
//     const canvasImage = new fabric.Canvas('canva-img');
//     canvasImage.setWidth(180);
//     canvasImage.setHeight(180);
//     canvasImage.renderAll()

//     const imgInstance = new fabric.Image(img1, {
//       left: 15, top: 10,
//     });

//     imgInstance.scaleToWidth(canvasImage.getWidth());
//     imgInstance.scaleToHeight(canvasImage.getHeight());

//     canvasImage.add(imgInstance);
//     imgInstance.selectable = false; // image is not movable

//     canvasImage.renderAll()
//     isExistCanvasImage.value = !isExistCanvasImage.value

//     // free draw rectangle
//     var rectangle, isDown, origX, origY;

//     canvasImage.on('mouse:down', function (o) {
//       var pointer = canvasImage.getPointer(o.e);

//       isDown = true;
//       origX = pointer.x;
//       origY = pointer.y;

//       rectangle = new fabric.Rect({
//         left: origX,
//         top: origY,
//         fill: 'transparent',
//         // stroke: '#6cffd6',
//         stroke: 'white',
//         strokeWidth: 2,
//       });
//       rectangle.selectable = false
//       canvasImage.add(rectangle);
//     });

//     canvasImage.on('mouse:move', function (o) {
//       if (!isDown) return;
//       var pointer = canvasImage.getPointer(o.e);
//       if (origX > pointer.x) {
//         rectangle.set({ left: Math.abs(pointer.x) });
//       }
//       if (origY > pointer.y) {
//         rectangle.set({ top: Math.abs(pointer.y) });
//       }

//       rectangle.set({ width: Math.abs(origX - pointer.x) });
//       rectangle.set({ height: Math.abs(origY - pointer.y) });
//       canvasImage.renderAll();
//     });

//     // 这个就是信号
//     canvasImage.on('mouse:up', function (o) {
//       isDown = false;
//       let param = {
//         // XYXY format
//         "box": [rectangle.left - 15, rectangle.top - 10, rectangle.left + rectangle.width - 15, rectangle.top + rectangle.height - 10],
//         "image_url": img1.src,
//         "mode": "image"
//       };

//       imageSegment(param, function (data) {
//         const imgEl = document.createElement('img');
//         imgEl.src = data.img
//         storeDesignPrior.shapeImage = data.shape
//         storeDesignPrior.colorImage = data.color
//         // 插入页面
//         document.body.appendChild(imgEl);
//         imgEl.onload = () => { // 必须要加onload，等图片加载完全，不然就是空的
//           canvasImage.clear();
//           const imgInstanceNew = new fabric.Image(imgEl, {
//             left: 15, top: 10,
//           });
//           // 设置缩放
//           imgInstanceNew.scaleToWidth(canvasImage.getWidth());
//           imgInstanceNew.scaleToHeight(canvasImage.getHeight());
//           imgInstanceNew.selectable = false;

//           canvasImage.add(imgInstanceNew)
//           canvasImage.renderAll()
//           // 删除页面中的图片元素
//           imgEl.remove()
//         }
//         canvasImage.renderAll()
//       })
//     });

//   };
// }
// // box
// function loadImageOrDisplay2() {
//   var img2 = document.getElementById("img2");
//   // 初始上传，点击上传本地文件
//   if (img2.src == "http://localhost/src/assets/upload_image/default1.png") {
//     document.getElementById('input-img2').click()
//     document.getElementById('input-img2').addEventListener('change', function (event) {
//       var file = event.target.files[0];
//       var reader = new FileReader();
//       reader.onload = function (event) {
//         img2.src = event.target.result;
//       };
//       reader.readAsDataURL(file);
//     });
//   }
//   // 已经上传好了，点击显示到canvas上
//   else {
//     // 删掉原有的canvas再新建一个，再加入fabric canvas
//     // fabric canvas 有两个，原先的这个canvas只是第一个，共同归属canvas-container管
//     var oldCanvas = document.getElementById("canva-img");
//     if (firstDisplay.value) {
//       oldCanvas.parentNode.removeChild(oldCanvas);
//       firstDisplay.value = false
//     }
//     else {
//       var parentElement = oldCanvas.parentNode;
//       var grandparentElement = parentElement.parentNode;
//       grandparentElement.removeChild(parentElement);
//     }

//     // add new canvas
//     const imgInputDiv = document.querySelector(".img-input");
//     const canvasImage0 = document.createElement("canvas")

//     canvasImage0.id = "canva-img";
//     canvasImage0.width = 180;
//     canvasImage0.height = 180;
//     imgInputDiv.appendChild(canvasImage0);

//     // add style for canvas
//     const style = document.createElement("style");
//     style.innerHTML = `
//     .canvas-container {
//       background-color: #ffffff;
//       padding: 5px 8px;
//       border-radius: 6px;
//       border: 1px solid #cacaca; }`;
//     document.head.appendChild(style);

//     // add image instance 
//     const canvasImage = new fabric.Canvas('canva-img');
//     canvasImage.setWidth(180);
//     canvasImage.setHeight(180);
//     canvasImage.renderAll()

//     const imgInstance = new fabric.Image(img2, {
//       left: 15, top: 10,
//     });

//     imgInstance.scaleToWidth(canvasImage.getWidth());
//     imgInstance.scaleToHeight(canvasImage.getHeight());

//     canvasImage.add(imgInstance);
//     imgInstance.selectable = false; // image is not movable

//     canvasImage.renderAll()
//     isExistCanvasImage.value = !isExistCanvasImage.value

//     // free draw rectangle
//     var rectangle, isDown, origX, origY;

//     canvasImage.on('mouse:down', function (o) {
//       var pointer = canvasImage.getPointer(o.e);

//       isDown = true;
//       origX = pointer.x;
//       origY = pointer.y;

//       rectangle = new fabric.Rect({
//         left: origX,
//         top: origY,
//         fill: 'transparent',
//         // stroke: '#6cffd6',
//         stroke: 'white',
//         strokeWidth: 2,
//       });
//       rectangle.selectable = false
//       canvasImage.add(rectangle);
//     });

//     canvasImage.on('mouse:move', function (o) {
//       if (!isDown) return;
//       var pointer = canvasImage.getPointer(o.e);
//       if (origX > pointer.x) {
//         rectangle.set({ left: Math.abs(pointer.x) });
//       }
//       if (origY > pointer.y) {
//         rectangle.set({ top: Math.abs(pointer.y) });
//       }

//       rectangle.set({ width: Math.abs(origX - pointer.x) });
//       rectangle.set({ height: Math.abs(origY - pointer.y) });
//       canvasImage.renderAll();
//     });

//     // 这个就是信号
//     canvasImage.on('mouse:up', function (o) {
//       isDown = false;
//       let param = {
//         // XYXY format
//         "box": [rectangle.left - 15, rectangle.top - 10, rectangle.left + rectangle.width - 15, rectangle.top + rectangle.height - 10],
//         "image_url": img2.src,
//         "mode": "image"
//       };

//       imageSegment(param, function (data) {
//         const imgEl = document.createElement('img');
//         imgEl.src = data.img
//         storeDesignPrior.shapeImage = data.shape
//         storeDesignPrior.colorImage = data.color
//         // 插入页面
//         document.body.appendChild(imgEl);
//         imgEl.onload = () => { // 必须要加onload，等图片加载完全，不然就是空的
//           canvasImage.clear();
//           const imgInstanceNew = new fabric.Image(imgEl, {
//             left: 15, top: 10,
//           });
//           // 设置缩放
//           imgInstanceNew.scaleToWidth(canvasImage.getWidth());
//           imgInstanceNew.scaleToHeight(canvasImage.getHeight());
//           imgInstanceNew.selectable = false;

//           canvasImage.add(imgInstanceNew)
//           canvasImage.renderAll()
//           // 删除页面中的图片元素
//           imgEl.remove()
//         }
//         canvasImage.renderAll()
//       })
//     });

//   };
// }
// // box
// function loadImageOrDisplay3() {
//   var img3 = document.getElementById("img3");
//   // 初始上传，点击上传本地文件
//   if (img3.src == "http://localhost/src/assets/upload_image/default1.png") {
//     document.getElementById('input-img3').click()
//     document.getElementById('input-img3').addEventListener('change', function (event) {
//       var file = event.target.files[0];
//       var reader = new FileReader();
//       reader.onload = function (event) {
//         img3.src = event.target.result;
//       };
//       reader.readAsDataURL(file);
//     });
//   }
//   // 已经上传好了，点击显示到canvas上
//   else {
//     // 删掉原有的canvas再新建一个，再加入fabric canvas
//     // fabric canvas 有两个，原先的这个canvas只是第一个，共同归属canvas-container管
//     var oldCanvas = document.getElementById("canva-img");
//     if (firstDisplay.value) {
//       oldCanvas.parentNode.removeChild(oldCanvas);
//       firstDisplay.value = false
//     }
//     else {
//       var parentElement = oldCanvas.parentNode;
//       var grandparentElement = parentElement.parentNode;
//       grandparentElement.removeChild(parentElement);
//     }

//     // add new canvas
//     const imgInputDiv = document.querySelector(".img-input");
//     const canvasImage0 = document.createElement("canvas")

//     canvasImage0.id = "canva-img";
//     canvasImage0.width = 180;
//     canvasImage0.height = 180;
//     imgInputDiv.appendChild(canvasImage0);

//     // add style for canvas
//     const style = document.createElement("style");
//     style.innerHTML = `
//     .canvas-container {
//       background-color: #ffffff;
//       padding: 5px 8px;
//       border-radius: 6px;
//       border: 1px solid #cacaca; }`;
//     document.head.appendChild(style);

//     // add image instance 
//     const canvasImage = new fabric.Canvas('canva-img');
//     canvasImage.setWidth(180);
//     canvasImage.setHeight(180);
//     canvasImage.renderAll()

//     const imgInstance = new fabric.Image(img3, {
//       left: 15, top: 10,
//     });

//     imgInstance.scaleToWidth(canvasImage.getWidth());
//     imgInstance.scaleToHeight(canvasImage.getHeight());

//     canvasImage.add(imgInstance);
//     imgInstance.selectable = false; // image is not movable

//     canvasImage.renderAll()
//     isExistCanvasImage.value = !isExistCanvasImage.value

//     // free draw rectangle
//     var rectangle, isDown, origX, origY;

//     canvasImage.on('mouse:down', function (o) {
//       var pointer = canvasImage.getPointer(o.e);

//       isDown = true;
//       origX = pointer.x;
//       origY = pointer.y;

//       rectangle = new fabric.Rect({
//         left: origX,
//         top: origY,
//         fill: 'transparent',
//         // stroke: '#6cffd6',
//         stroke: 'white',
//         strokeWidth: 2,
//       });
//       rectangle.selectable = false
//       canvasImage.add(rectangle);
//     });

//     canvasImage.on('mouse:move', function (o) {
//       if (!isDown) return;
//       var pointer = canvasImage.getPointer(o.e);
//       if (origX > pointer.x) {
//         rectangle.set({ left: Math.abs(pointer.x) });
//       }
//       if (origY > pointer.y) {
//         rectangle.set({ top: Math.abs(pointer.y) });
//       }

//       rectangle.set({ width: Math.abs(origX - pointer.x) });
//       rectangle.set({ height: Math.abs(origY - pointer.y) });
//       canvasImage.renderAll();
//     });

//     // 这个就是信号
//     canvasImage.on('mouse:up', function (o) {
//       isDown = false;
//       let param = {
//         // XYXY format
//         "box": [rectangle.left - 15, rectangle.top - 10, rectangle.left + rectangle.width - 15, rectangle.top + rectangle.height - 10],
//         "image_url": img3.src,
//         "mode": "image"
//       };

//       imageSegment(param, function (data) {
//         const imgEl = document.createElement('img');
//         imgEl.src = data.img
//         storeDesignPrior.shapeImage = data.shape
//         storeDesignPrior.colorImage = data.color
//         // 插入页面
//         document.body.appendChild(imgEl);
//         imgEl.onload = () => { // 必须要加onload，等图片加载完全，不然就是空的
//           canvasImage.clear();
//           const imgInstanceNew = new fabric.Image(imgEl, {
//             left: 15, top: 10,
//           });
//           // 设置缩放
//           imgInstanceNew.scaleToWidth(canvasImage.getWidth());
//           imgInstanceNew.scaleToHeight(canvasImage.getHeight());
//           imgInstanceNew.selectable = false;

//           canvasImage.add(imgInstanceNew)
//           canvasImage.renderAll()
//           // 删除页面中的图片元素
//           imgEl.remove()
//         }
//         canvasImage.renderAll()
//       })
//     });

//   };
// }

// anchor
function loadImageOrDisplay1() {
  var img1 = document.getElementById("img1");
  // 初始上传，点击上传本地文件
  if (img1.src == "http://localhost/src/assets/upload_image/default1.png") {
    document.getElementById('input-img1').click()
    document.getElementById('input-img1').addEventListener('change', function (event) {
      var file = event.target.files[0];
      var reader = new FileReader();
      reader.onload = function (event) {
        img1.src = event.target.result;
      };
      reader.readAsDataURL(file);
    });
  }
  // 已经上传好了，点击显示到canvas上
  else {
    // 删掉原有的canvas再新建一个，再加入fabric canvas
    // fabric canvas 有两个，原先的这个canvas只是第一个，共同归属canvas-container管
    var oldCanvas = document.getElementById("canva-img");
    if (firstDisplay.value) {
      oldCanvas.parentNode.removeChild(oldCanvas);
      firstDisplay.value = false
    }
    else {
      var parentElement = oldCanvas.parentNode;
      var grandparentElement = parentElement.parentNode;
      grandparentElement.removeChild(parentElement);
    }

    // add new canvas
    const imgInputDiv = document.querySelector(".img-input");
    const canvasImage0 = document.createElement("canvas")

    canvasImage0.id = "canva-img";
    canvasImage0.width = 180;
    canvasImage0.height = 180;
    imgInputDiv.appendChild(canvasImage0);

    // add style for canvas
    const style = document.createElement("style");
    style.innerHTML = `
    .canvas-container {
      background-color: #ffffff;
      padding: 5px 8px;
      border-radius: 6px;
      border: 1px solid #D8D2B3; }`;
    document.head.appendChild(style);

    // add image instance 
    const canvasImage = new fabric.Canvas('canva-img');
    canvasImage.setWidth(180);
    canvasImage.setHeight(180);
    canvasImage.renderAll()

    const imgInstance = new fabric.Image(img1, {
      left: 15, top: 10,
    });

    imgInstance.scaleToWidth(canvasImage.getWidth());
    imgInstance.scaleToHeight(canvasImage.getHeight());

    canvasImage.add(imgInstance);
    imgInstance.selectable = false; // image is not movable

    // canvasImage.renderAll()
    isExistCanvasImage.value = !isExistCanvasImage.value

    // free draw rectangle
    var origX, origY;
    let inputPoints = [];

    canvasImage.on('mouse:down', function (o) {
      var pointer = canvasImage.getPointer(o.e);

      origX = pointer.x;
      origY = pointer.y;
      inputPoints.push([origX - 15, origY - 10])

      const anchorImg = document.createElement('img');
      anchorImg.src = "src/assets/upload_image/anchor.png"
      // 插入页面
      document.body.appendChild(anchorImg);
      anchorImg.onload = () => { // 必须要加onload，等图片加载完全，不然就是空的
        // canvasImage.clear();
        const anchorInstance = new fabric.Image(anchorImg, {
          left: origX - 15,
          top: origY - 10,
        });

        // anchorInstance.scaleToWidth(canvasImage.getWidth());
        // anchorInstance.scaleToHeight(canvasImage.getHeight());
        canvasImage.add(anchorInstance);
        anchorInstance.selectable = false; // image is not movable
        // canvasImage.renderAll()
        anchorImg.remove()
      }
    });

    // 这个就是信号
    canvasImage.on('mouse:up', function (o) {
      let param = {
        // XYXY format
        "points": inputPoints,
        "image_url": img1.src,
        "mode": "image"
      };

      imageSegment(param, function (data) {
        const imgEl = document.createElement('img');
        imgEl.src = data
        // storeDesignPrior.shapeImage = data.shape
        // storeDesignPrior.colorImage = data.color
        // 插入页面
        document.body.appendChild(imgEl);
        imgEl.onload = () => { // 必须要加onload，等图片加载完全，不然就是空的
          canvasImage.clear();
          const imgInstanceNew = new fabric.Image(imgEl, {
            left: 15, top: 10,
          });
          // 设置缩放
          imgInstanceNew.scaleToWidth(canvasImage.getWidth());
          imgInstanceNew.scaleToHeight(canvasImage.getHeight());
          imgInstanceNew.selectable = false;

          canvasImage.add(imgInstanceNew)
          canvasImage.renderAll()
          // 删除页面中的图片元素
          imgEl.remove()
        }
        canvasImage.renderAll()
      })
    });

  };
}
function loadImageOrDisplay2() {
  var img2 = document.getElementById("img2");
  // 初始上传，点击上传本地文件
  if (img2.src == "http://localhost/src/assets/upload_image/default1.png") {
    document.getElementById('input-img2').click()
    document.getElementById('input-img2').addEventListener('change', function (event) {
      var file = event.target.files[0];
      var reader = new FileReader();
      reader.onload = function (event) {
        img2.src = event.target.result;
      };
      reader.readAsDataURL(file);
    });
  }
  // 已经上传好了，点击显示到canvas上
  else {
    // 删掉原有的canvas再新建一个，再加入fabric canvas
    // fabric canvas 有两个，原先的这个canvas只是第一个，共同归属canvas-container管
    var oldCanvas = document.getElementById("canva-img");
    if (firstDisplay.value) {
      oldCanvas.parentNode.removeChild(oldCanvas);
      firstDisplay.value = false
    }
    else {
      var parentElement = oldCanvas.parentNode;
      var grandparentElement = parentElement.parentNode;
      grandparentElement.removeChild(parentElement);
    }

    // add new canvas
    const imgInputDiv = document.querySelector(".img-input");
    const canvasImage0 = document.createElement("canvas")

    canvasImage0.id = "canva-img";
    canvasImage0.width = 180;
    canvasImage0.height = 180;
    imgInputDiv.appendChild(canvasImage0);

    // add style for canvas
    const style = document.createElement("style");
    style.innerHTML = `
    .canvas-container {
      background-color: #ffffff;
      padding: 5px 8px;
      border-radius: 6px;
      border: 1px solid #D8D2B3; }`;
    document.head.appendChild(style);

    // add image instance 
    const canvasImage = new fabric.Canvas('canva-img');
    canvasImage.setWidth(180);
    canvasImage.setHeight(180);
    canvasImage.renderAll()

    const imgInstance = new fabric.Image(img2, {
      left: 15, top: 10,
    });

    imgInstance.scaleToWidth(canvasImage.getWidth());
    imgInstance.scaleToHeight(canvasImage.getHeight());

    canvasImage.add(imgInstance);
    imgInstance.selectable = false; // image is not movable

    // canvasImage.renderAll()
    isExistCanvasImage.value = !isExistCanvasImage.value

    // free draw rectangle
    var origX, origY;
    let inputPoints = [];

    canvasImage.on('mouse:down', function (o) {
      var pointer = canvasImage.getPointer(o.e);

      origX = pointer.x;
      origY = pointer.y;
      inputPoints.push([origX - 15, origY - 10])

      const anchorImg = document.createElement('img');
      anchorImg.src = "src/assets/upload_image/anchor.png"
      // 插入页面
      document.body.appendChild(anchorImg);
      anchorImg.onload = () => { // 必须要加onload，等图片加载完全，不然就是空的
        // canvasImage.clear();
        const anchorInstance = new fabric.Image(anchorImg, {
          left: origX - 15,
          top: origY - 10,
        });

        // anchorInstance.scaleToWidth(canvasImage.getWidth());
        // anchorInstance.scaleToHeight(canvasImage.getHeight());
        canvasImage.add(anchorInstance);
        anchorInstance.selectable = false; // image is not movable
        // canvasImage.renderAll()
        anchorImg.remove()
      }
    });

    // 这个就是信号
    canvasImage.on('mouse:up', function (o) {
      let param = {
        // XYXY format
        "points": inputPoints,
        "image_url": img2.src,
        "mode": "image"
      };

      imageSegment(param, function (data) {
        const imgEl = document.createElement('img');
        imgEl.src = data
        // storeDesignPrior.shapeImage = data.shape
        // storeDesignPrior.colorImage = data.color
        // 插入页面
        document.body.appendChild(imgEl);
        imgEl.onload = () => { // 必须要加onload，等图片加载完全，不然就是空的
          canvasImage.clear();
          const imgInstanceNew = new fabric.Image(imgEl, {
            left: 15, top: 10,
          });
          // 设置缩放
          imgInstanceNew.scaleToWidth(canvasImage.getWidth());
          imgInstanceNew.scaleToHeight(canvasImage.getHeight());
          imgInstanceNew.selectable = false;

          canvasImage.add(imgInstanceNew)
          canvasImage.renderAll()
          // 删除页面中的图片元素
          imgEl.remove()
        }
        canvasImage.renderAll()
      })
    });

  };
}
function loadImageOrDisplay3() {
  var img3 = document.getElementById("img3");
  // 初始上传，点击上传本地文件
  if (img3.src == "http://localhost/src/assets/upload_image/default1.png") {
    document.getElementById('input-img3').click()
    document.getElementById('input-img3').addEventListener('change', function (event) {
      var file = event.target.files[0];
      var reader = new FileReader();
      reader.onload = function (event) {
        img3.src = event.target.result;
      };
      reader.readAsDataURL(file);
    });
  }
  // 已经上传好了，点击显示到canvas上
  else {
    // 删掉原有的canvas再新建一个，再加入fabric canvas
    // fabric canvas 有两个，原先的这个canvas只是第一个，共同归属canvas-container管
    var oldCanvas = document.getElementById("canva-img");
    if (firstDisplay.value) {
      oldCanvas.parentNode.removeChild(oldCanvas);
      firstDisplay.value = false
    }
    else {
      var parentElement = oldCanvas.parentNode;
      var grandparentElement = parentElement.parentNode;
      grandparentElement.removeChild(parentElement);
    }

    // add new canvas
    const imgInputDiv = document.querySelector(".img-input");
    const canvasImage0 = document.createElement("canvas")

    canvasImage0.id = "canva-img";
    canvasImage0.width = 180;
    canvasImage0.height = 180;
    imgInputDiv.appendChild(canvasImage0);

    // add style for canvas
    const style = document.createElement("style");
    style.innerHTML = `
    .canvas-container {
      background-color: #ffffff;
      padding: 5px 8px;
      border-radius: 6px;
      border: 1px solid #D8D2B3; }`;
    document.head.appendChild(style);

    // add image instance 
    const canvasImage = new fabric.Canvas('canva-img');
    canvasImage.setWidth(180);
    canvasImage.setHeight(180);
    canvasImage.renderAll()

    const imgInstance = new fabric.Image(img3, {
      left: 15, top: 10,
    });

    imgInstance.scaleToWidth(canvasImage.getWidth());
    imgInstance.scaleToHeight(canvasImage.getHeight());

    canvasImage.add(imgInstance);
    imgInstance.selectable = false; // image is not movable

    // canvasImage.renderAll()
    isExistCanvasImage.value = !isExistCanvasImage.value

    // free draw rectangle
    var origX, origY;
    let inputPoints = [];

    canvasImage.on('mouse:down', function (o) {
      var pointer = canvasImage.getPointer(o.e);

      origX = pointer.x;
      origY = pointer.y;
      inputPoints.push([origX - 15, origY - 10])

      const anchorImg = document.createElement('img');
      anchorImg.src = "src/assets/upload_image/anchor.png"
      // 插入页面
      document.body.appendChild(anchorImg);
      anchorImg.onload = () => { // 必须要加onload，等图片加载完全，不然就是空的
        // canvasImage.clear();
        const anchorInstance = new fabric.Image(anchorImg, {
          left: origX - 15,
          top: origY - 10,
        });

        // anchorInstance.scaleToWidth(canvasImage.getWidth());
        // anchorInstance.scaleToHeight(canvasImage.getHeight());
        canvasImage.add(anchorInstance);
        anchorInstance.selectable = false; // image is not movable
        // canvasImage.renderAll()
        anchorImg.remove()
      }
    });

    // 这个就是信号
    canvasImage.on('mouse:up', function (o) {
      let param = {
        // XYXY format
        "points": inputPoints,
        "image_url": img3.src,
        "mode": "image"
      };

      imageSegment(param, function (data) {
        const imgEl = document.createElement('img');
        imgEl.src = data
        // storeDesignPrior.shapeImage = data.shape
        // storeDesignPrior.colorImage = data.color
        // 插入页面
        document.body.appendChild(imgEl);
        imgEl.onload = () => { // 必须要加onload，等图片加载完全，不然就是空的
          canvasImage.clear();
          const imgInstanceNew = new fabric.Image(imgEl, {
            left: 15, top: 10,
          });
          // 设置缩放
          imgInstanceNew.scaleToWidth(canvasImage.getWidth());
          imgInstanceNew.scaleToHeight(canvasImage.getHeight());
          imgInstanceNew.selectable = false;

          canvasImage.add(imgInstanceNew)
          canvasImage.renderAll()
          // 删除页面中的图片元素
          imgEl.remove()
        }
        canvasImage.renderAll()
      })
    });

  };
}


function startExtract() {
  let param = "123"
  startImageExtract(param, function (data) {
    storeDesignPrior.semanticImage = data.semantic,
      storeDesignPrior.colorImage = data.color,
      storeDesignPrior.shapeImage = data.shape,
      storeDesignPrior.shapePrompt = data.semantic_prompt,
      // storeDesignPrior.svgString = data.svg_string,
      storeDesignPrior.sampledPoints = data.sampled_points,
      eventBus.emit("isExtract", {
        "message": "show design prior in Generate view",
      })
  })
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="less">
:deep(.ivu-tooltip-inner) {
  white-space: normal;
}

:deep(.ivu-tooltip) {
  display: block;
}

:deep(.ivu-tooltip-rel) {
  display: block;
}

// .wordView {
//   width: 100%;
//   height: 33%;
//   margin-top: -41px;
//   background: #fff;
//   position: relative;
//   z-index: 1;
//   vertical-align: auto;
// }

// .ideaView {
//   width: 100%;
//   height: 22%;
//   margin-top: -25px;
//   background: #fff;
// }

.wordView {
  width: 100%;
  height: 33%;
  margin-top: -25px;
  background: #fff;
  position: relative;
  z-index: 1;
  vertical-align: auto;
}

.ideaView {
  width: 100%;
  height: 22%;
  margin-top: -41px;
  background: #fff;
}

.imageView {
  width: 100%;
  height: 29%;
  margin-top: -25px;
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

.text-word {
  // margin-top: 10px;
  // margin-left: 2px;
  width: 90%;
  height: 22px;
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
  font-size: 14px;
  line-height: 1.4em;
  padding: 5px 8px;
  transition: background-color 0.2s ease 0s;
}

.text-word:focus {
  background: none repeat scroll 0 0 #f9f9f9;
  outline-width: 0;
}

.text-idea {
  // margin-top: 10px;
  // margin-left: 2px;
  width: 89%;
  height: 44px;
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
  font-size: 14px;
  line-height: 1.4em;
  padding: 5px 8px;
  transition: background-color 0.2s ease 0s;
}

.text-idea:focus {
  background: none repeat scroll 0 0 #f9f9f9;
  outline-width: 0;
}

.button-idea {
  // display: inline-block;
  // padding-left: 5px;
  margin-right: 11px;
  background-color: #EDEFAB;
  width: 68px;
  height: 52px;
  border-radius: 4px;
  text-align: center;
  /* 将文本水平居中 */
  font-size: 13px;
  color: #797B0B;
  /* 设置字体大小为10px */
  line-height: 13px;
}

.tags {
  list-style: none;
  margin: 0;
  overflow: hidden;
  padding: 0;
  font-size: 13px;
  margin-top: 5px;
}

.tags li {
  float: left;
}

.tag {
  background: #F7F6F0;
  border-radius: 3px 0 0 3px;
  color: #797B0B;
  display: inline-block;
  height: 20px;
  line-height: 20px;
  padding: 0 15px 0 8px;
  position: relative;
  margin: 0 10px 5px 0;
  text-decoration: none;
  // -webkit-transition: color 0.2s;
}

// .tag::before {
//   background: #fff;
//   border-radius: 10px;
//   box-shadow: inset 0 1px rgba(0, 0, 0, 0.25);
//   content: '';
//   height: 6px;
//   left: 10px;
//   position: absolute;
//   width: 6px;
//   top: 10px;
// }

.tag::after {
  background: #fff;
  border-bottom: 10px solid transparent;
  border-left: 9px solid #F7F6F0;
  border-top: 11px solid transparent;
  content: '';
  position: absolute;
  right: 0;
  top: 0;
}

.tag:hover {
  background-color: #EDEFAB;
  // color: white;
  color: #797B0B;
}

.tooltip {
  position: absolute;
  background-color: rgba(0, 0, 0, 0.8);
  color: white;
  padding: 8px;
  border-radius: 4px;
}

.tag:hover::after {
  border-left-color: #EDEFAB;
  color: #797B0B;
}

.upload-img {
  padding: 0px;
  margin-left: -10px;
  margin-right: 5px;
  margin-bottom: 6px;
  width: 50px;
  height: 50px;
  border-radius: 10px;
}

.upload-img img {
  border-radius: 6px;
}

input[type="file"] {
  display: none;
}

.lassoButton-img {
  // display: inline-block;
  background-color: #EDEFAB;
  margin-left: -10px;
  // padding-left: 7px;
  // margin-right: 11px;
  width: 50px;
  height: 22px;
  border-radius: 4px;
  text-align: center;
  font-size: 13px;
  color: #797B0B;
  /* 设置字体大小为10px */
  line-height: 2px;
  /* 设置行高等于按钮的高度，以实现垂直居中 */
}

.lassoButton-img>.icon-function-small path {
  fill: #797B0B;
}

.icon-function-small {
  margin-top: -5px;
  width: 14px;
  height: 14px
}

.canva-word-container {
  width: 89%;
}

canvas {
  // canvas的长宽不要通过css来设，直接在html申明
  background-color: #ffffff;
  padding: 5px 8px;
  border-radius: 6px;
  border: 1px solid #d8d2b3;
}

.word-options {
  display: flex;
  align-items: center;
  /* 将按钮容器中的内容垂直居中 */
  margin-bottom: 5px;
}

.inline-button {
  display: inline-block;
  margin-right: 5px;
  // /* 可调整按钮之间的间距 */ F5F5F5
  background-color: #EDEFAB;
  width: 60px;
  height: 24px;
  border-radius: 4px;
  text-align: center;
  /* 将文本水平居中 */
  font-size: 13px;
  color: #797B0B;
  /* 设置字体大小为10px */
  line-height: 3px;
  /* 设置行高等于按钮的高度，以实现垂直居中 */
}

.inline-button>.icon-function path {
  fill: #797B0B;
}

.icon-function {
  margin-top: -5px;
  width: 16px;
  height: 16px
}

.title-btn {
  background-color: #EDEFAB;
  border: none;
  border-radius: 5px;
  color: white;
  padding: 4px 4px;
  font-size: 18px;
  margin-right: 5px;
}

/* Darker background on mouse-over */
.title-btn.active {
  background-color: #EEF9FF;
  border: 15px;
  border-color: #a1a1a1;
}

// .btn:focus svg {
//   // color: #465EEA;
//   color: #465EEA;
// }
.title-btn>.icon path {
  fill: #797B0B;
}

.icon {
  width: 20px;
  height: 20px
}


input[type="text"],
select {
  // display: block;
  width: 40%;
  color: #6F6E7E;
  height: 24px;
  padding: 3px;
  padding-left: 12%;
  font-size: 13px;
  border-radius: 5px;
  border: 1.5px solid #E1E4EB;
  margin-bottom: 0px;
  box-sizing: border-box;
}

.button-8 {
  width: 80%;
  height: 23px;
  background-color: #d6eaf4; //e1ecf4
  border-radius: 3px;
  border: 0px solid #EEF9FF; //#7aa7c7
  // box-shadow: rgba(255, 255, 255, .7) 0 1px 0 0 inset;
  box-sizing: border-box;
  color: #39739d;
  cursor: pointer;
  display: flex;
  align-items: center;
  /* 垂直居中 */
  justify-content: center;
  /* 水平居中 */
  font-family: -apple-system, system-ui, "Segoe UI", "Liberation Sans", sans-serif;
  font-size: 13px;
  font-weight: 600;
  line-height: 1.15385;
  margin: 0;
  outline: none;
  // padding: 8px 8px;
  // position: relative;
  // text-align: center;
  text-decoration: none;
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
  vertical-align: baseline;
  white-space: nowrap;
}

.button-8:hover {
  background-color: #b3d3ea;
  color: #2c5777;
}

.button-8:active {
  background-color: #a0c7e4;
  box-shadow: none;
  // color: #2c5777;
}

button {
  background-color: #ccc;
  padding: 10px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}
</style>
