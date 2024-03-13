<!--
 * @Author: 秦少卫
 * @Date: 2022-09-03 19:16:55
 * @LastEditors: 秦少卫
 * @LastEditTime: 2022-09-06 23:20:40
 * @Description: 图层面板
-->

<template>
  <div class="gallery">
    <h3 class="h3Generate">
      <button class="title-btn">
        <svg t="1690349527043" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg"
          p-id="33085">
          <path
            d="M322.236144 725.261686c-17.379654-17.379654-8.319834-12.479752-50.239-23.699529-19.019621-5.099899-35.739289-14.899703-50.858988-26.63947L130.399962 897.39826c-8.779825 21.539571 7.619848 44.939106 30.859386 44.059123l105.377903-4.01992L339.115808 1013.995939c15.999682 16.879664 44.079123 11.619769 52.858948-9.919802l104.097928-255.234921c-21.679569 12.07976-45.73909 19.159619-70.618594 19.159619-38.999224 0-75.638495-15.179698-103.217946-42.739149zM893.584773 897.39826l-90.738194-222.475573c-15.119699 11.759766-31.839366 21.539571-50.858988 26.63947-42.139161 11.279776-32.899345 6.359873-50.239 23.699529-27.579451 27.559452-64.238721 42.739149-103.237945 42.739149-24.879505 0-48.939026-7.099859-70.618595-19.159619L631.989979 1004.076137c8.779825 21.539571 36.879266 26.799467 52.858948 9.919802l72.498558-76.558476 105.377902 4.01992c23.239537 0.879982 39.639211-22.539551 30.859386-44.059123zM653.989542 680.002586c30.559392-31.099381 34.059322-28.419434 77.578456-40.279198 27.779447-7.579849 49.499015-29.679409 56.938866-57.958846 14.959702-56.79887 11.079779-49.939006 51.898967-91.498179 20.339595-20.699588 28.279437-50.878987 20.839586-79.158425-14.939703-56.75887-14.959702-48.839028 0-105.657897 7.439852-28.279437-0.49999-58.458837-20.839586-79.158425-40.819188-41.559173-36.939265-34.719309-51.898967-91.498179-7.439852-28.279437-29.15942-50.378997-56.938866-57.958846-55.75889-15.219697-49.039024-11.239776-89.898211-52.818949-20.339595-20.699588-49.999005-28.799427-77.778452-21.219578-55.738891 15.199697-47.959046 15.219697-103.797934 0-27.779447-7.579849-57.438857 0.49999-77.778452 21.219578-40.819188 41.559173-34.099321 37.599252-89.878212 52.818949-27.779447 7.579849-49.499015 29.679409-56.938866 57.958846-14.939703 56.77887-11.079779 49.939006-51.898968 91.498179-20.339595 20.699588-28.299437 50.878987-20.839585 79.158425 14.939703 56.718871 14.959702 48.799029 0 105.637897-7.439852 28.279437 0.49999 58.458837 20.839585 79.178425 40.819188 41.559173 36.939265 34.699309 51.898968 91.498179 7.439852 28.279437 29.15942 50.378997 56.938866 57.958846C337.195847 651.923145 340.53578 650.003183 369.995194 680.002586c26.459473 26.939464 67.678653 31.759368 99.47802 11.639769a79.350421 79.350421 0 0 1 85.058307 0c31.779368 20.1196 72.998547 15.299696 99.458021-11.639769zM323.316123 351.929116c0-106.057889 84.478319-192.036178 188.676245-192.036178s188.676245 85.978289 188.676245 192.036178-84.478319 192.036178-188.676245 192.036178-188.676245-85.978289-188.676245-192.036178z"
            p-id="33086"></path>
        </svg> </button>
      <span>GALLERY -------------------------------------------------</span>
    </h3>

    <div class="gallery-result" style="display: flex; flex-direction: column; padding-left: 10px; ">
      <!-- <div class="gallery-row">
        <div class="info">
          <div class="prompt-info">wezi</div>
          <div class="image-info">
            <div class="cache-img-word"><img src="" alt=""></div>
            <div class="cache-img-image"><img src="" alt=""></div>
            <div class="option-labels">
              <button class="option-label-semantic" v-if="showSemantic">
              </button>
              <button class="option-label-color" v-if="showColor">
              </button>
              <button class="option-label-shape" v-if="showShape">
              </button>
            </div>
          </div>
        </div>

        <div class="gallery-group">
          <div class="gallery-item">
            <img src="" alt="">
            <button class="gallery-item-button" role="button">X</button>
          </div>
          <div class="gallery-item">
            <img src="" alt="">
            <button class="gallery-item-button" role="button">X</button>
          </div>
          <div class="gallery-item">
            <img src="" alt="">
            <button class="gallery-item-button" role="button">X</button>
          </div>
          <div class="gallery-item">
            <img src="" alt="">
            <button class="gallery-item-button" role="button">X</button>
          </div>
        </div>
      </div> -->


    </div>
  </div>
</template>
  
<script setup>
import { ref } from 'vue'; // import ref from vue 
import { px } from 'framer-motion';
import { useI18n } from 'vue-i18n';
import mitt from 'mitt';
import { method } from 'lodash';
import { useGenerateStore } from '../store/modules/generateStore';


const eventBus = inject("eventBus")
const isAddRow = ref(false);
let showSemantic = ref(false)
let showColor = ref(false)
let showShape = ref(false)

const store = useGenerateStore()
const canvas = inject("canvas")

onMounted(() => {
  eventBus.on("isGenerate", (data) => {
    console.log(data)
    if (data.addRow == true) {
      console.log("yes, add a row")
      addRow(data);
    }
    else {
      // console.log(data.addRow)
      console.log("no, not a row")
      modifyRow(data);
    }
  });
})

function clickRow(event) {
  // add background for highlight
  const gallery = document.querySelector('.gallery');
  const prevGrayRow = gallery.querySelector('.row-background');
  if (prevGrayRow) {
    prevGrayRow.classList.remove('row-background');
  }
  event.currentTarget.classList.add('row-background');
  // text 回溯
  const promptInfo = event.currentTarget.querySelector('.prompt-info').textContent;
  store.promptInfo = promptInfo;
  // label 回溯
  const semanticLabel = event.currentTarget.querySelector('.option-label-semantic');
  if (semanticLabel) { store.semanticLabel = true; } else { store.semanticLabel = false; }
  const colorLabel = event.currentTarget.querySelector('.option-label-color');
  if (colorLabel) { store.colorLabel = true; } else { store.colorLabel = false; }
  const shapeLabel = event.currentTarget.querySelector('.option-label-shape');
  if (shapeLabel) { store.shapeLabel = true; } else { store.shapeLabel = false; }
  // label图片 回溯 通过id
  const row = event.currentTarget;
  store.rowId = row.getAttribute('id')

  // 还要生成几张图
  const totalItems = event.currentTarget.querySelectorAll('.gallery-item').length;
  const emptyItems = event.currentTarget.querySelectorAll('.gallery-item:not(:has(img))').length;
  const numEmptyItems = totalItems - emptyItems;
  store.generateNum = emptyItems
  // console.log(numEmptyItems);
  eventBus.emit("backTracking", {
    message: "previous state of generation."
  });
  store.isClickRow = numEmptyItems

  // 获取当前的 mode list & img list
  let rowModeList = []
  let rowImageList = []
  // 获取当前row中所有的gallery-item
  const items = row.querySelectorAll('.gallery-item');
  items.forEach(item => {
    if (item.querySelector('img')) {
      let itemImage = item.querySelector("img");

      let name = itemImage.getAttribute('data-name');
      rowModeList.push(name);
      store.rowModeList = rowModeList;

      let imgContent = itemImage.getAttribute('src');
      rowImageList.push(imgContent);
      store.rowImageList = rowImageList;
    }
  })
  console.log(store.rowModeList)
}

function modifyRow(data) {
  // 获取具有row-background类的元素，也就是当前被点击的gallery-row
  const row = document.querySelector('.row-background');

  // 获取当前row中所有的gallery-item
  const items = row.querySelectorAll('.gallery-item');

  // 遍历items数组，查找哪些item没有img
  let i = 0
  items.forEach(item => {
    if (!item.querySelector('img')) {
      item.innerHTML = `<img src=${data.imgList[i]} data-name=${data.modeList[0]} data-alt=${data.alt}>` + item.innerHTML;
      i++;
    }
  });
  const imgButtons = row.querySelectorAll('.gallery-item-button');
  imgButtons.forEach(button => {
    const img = button.previousElementSibling;
    img.addEventListener('click', () => {
      const imgAlt = img.getAttribute("data-alt")
      fabric.Image.fromURL(img.src, function (imgInstance) {
        imgInstance.set({
          name: imgAlt
        });
        canvas.c.add(imgInstance);
      });
    });
    button.addEventListener('click', () => {
      img.remove();
      // button.remove(); 
    });
  });

}

function delete_option_label(name) {
  const Button = document.querySelector(name);
  if (Button) {
    Button.parentNode.removeChild(Button);
  }
}

const addRow = (data) => {
  showSemantic.value = data.semanticOption;
  showColor.value = data.colorOption;
  showShape.value = data.shapeOption;

  // Get the gallery element
  const gallery = document.querySelector('.gallery-result');

  // Create a new gallery-row element 
  const newRow = document.createElement('div');
  newRow.classList.add('gallery-row');
  newRow.setAttribute("id", data.id)
  newRow.addEventListener('click', clickRow);
  // Add the info element to the new row
  const newInfo = document.createElement('div');
  newInfo.classList.add('info');

  let semanticInnerHTML = ``
  let colorInnerHTML = ``
  let shapeInnerHTML = ``
  if (data.semanticOption) {
    semanticInnerHTML = `
        <button class="option-label-semantic" v-if="showSemantic">
          </button>`;
  } else { semanticInnerHTML = `` }

  if (data.colorOption) {
    colorInnerHTML = `
        <button class="option-label-color" v-if="showColor">
          </button>`;
  }
  if (data.shapeOption) {
    shapeInnerHTML = `
        <button class="option-label-shape" v-if="showShape">
          </button>`;
  }

  newInfo.innerHTML = `
  <textarea rows="2" cols="21" class="prompt-info">${data.prompt}</textarea>  
  <div class="image-info">
    <div class="cache-img-word"><img src=${data.word} alt=""></div>
      <div class="cache-img-image"><img src=${data.image} alt=""></div>
  ` + `<div class="option-labels">` + semanticInnerHTML + colorInnerHTML
    + shapeInnerHTML + ` </div> </div> </div>`

  newRow.appendChild(newInfo);

  // Add the gallery-group element to the new row
  const newGalleryGroup = document.createElement('div');
  newGalleryGroup.classList.add('gallery-group');
  newGalleryGroup.innerHTML = `
  <div class="gallery-item">  
    <img src=${data.imgList[0]} data-name=${data.modeList[0]} data-alt=${data.alt}>
    <button class="gallery-item-button" role="button">X</button>  
  </div>  
  <div class="gallery-item">  
    <img src=${data.imgList[1]} data-name=${data.modeList[0]} data-alt=${data.alt}>
    <button class="gallery-item-button" role="button">X</button>  
  </div>  
  <div class="gallery-item">  
    <img src=${data.imgList[2]} data-name=${data.modeList[0]} data-alt=${data.alt}>
    <button class="gallery-item-button" role="button">X</button>  
  </div>  
  <div class="gallery-item">  
    <img src=${data.imgList[3]} data-name=${data.modeList[0]} data-alt=${data.alt}>
    <button class="gallery-item-button" role="button">X</button>  
  </div>  
`;
  newRow.appendChild(newGalleryGroup);

  // 给img加上监听事件
  const galleryRows = document.querySelectorAll('.gallery-row');
  for (let i = 0; i < galleryRows.length; i++) {
    console.log(i)
    const img = galleryRows[i].querySelector('img');
    img.addEventListener('click', () => {
      console.log("点击img")
    });
  }

  // Insert the new row before the first row 
  const firstRow = gallery.querySelector('.gallery-row');
  gallery.insertBefore(newRow, firstRow);

  const imgButtons = newRow.querySelectorAll('.gallery-item-button');
  imgButtons.forEach(button => {
    const img = button.previousElementSibling;
    img.addEventListener('click', () => {
      const imgAlt = img.getAttribute("data-alt")
      fabric.Image.fromURL(img.src, function (imgInstance) {
        imgInstance.set({  // 设置图片属性
          name: imgAlt // 添加名字
        });
        canvas.c.add(imgInstance);
      });
    });
    button.addEventListener('click', () => {
      img.remove();
      // button.remove(); 
    });
  });
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="less">
:deep(.ivu-tooltip-inner) {
  white-space: normal;
}

:deep(.ivu-tooltip) {
  display: block;
}

:deep(.ivu-tooltip-rel) {
  display: block;
}

.gallery {
  width: 97.5%;
  height: 100%;
  margin-top: -30px;
  margin-left: 13px;
  margin-right: 5px;
  background: #fff;
}

.h3Generate {
  margin-top: 30px;
  text-align: left;
  text-transform: uppercase;
  background: #fff;
  padding-top: 5px;
  padding-left: 10px;

  font-family: "DM Sans", sans-serif;
  color: #2a2a2a;
  font-size: 16px;
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

// gallery

.gallery-row:focus {
  box-shadow: inset 0 0 3px #c4c4c4;
}

.gallery-row {
  display: flex;
  width: 424px;
  height: 70px;
  justify-content: center;
  align-items: center;
  border-radius: 7px;
  // border: 1px solid rgb(181, 181, 181);
  background-color: #F7F6F0;
  // border: 1px solid #b5b5b5;
  padding: 8px;
  margin: 0px auto;
  margin-left: 0px;
  margin-bottom: 10px;
}

.row-background {
  // box-shadow: inset 0 0 3px #7e7e7e;
  // border: 1px solid #a39d7c;
  // background: #e8e3cf;
  background: #f4f0dd;
}

.gallery-result::-webkit-scrollbar {
  width: 5px;
  /* width of the entire scrollbar */
}

.gallery-result::-webkit-scrollbar-track {
  background: #F7F6F0;
  /* color of the tracking area */
}

.gallery-result::-webkit-scrollbar-thumb {
  background-color: #d8d2b3;
  /* color of the scroll thumb */
  border-radius: 5px;
  /* roundness of the scroll thumb */
}

.gallery-result {
  overflow-y: scroll;
  /* add a scrollbar to the y-axis */
  width: 455px;
  // margin: 1%;
  margin-top: 10px;
  height: 190px;
  background-color: white;
}

.info {
  width: 130px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  /* horizontally center contents */
  align-items: center;
  /* vertically center contents */
}

.prompt-info {
  // margin-top: 10px;
  // margin-left: 2px;
  width: 119px;
  height: 22px;
  background: none repeat scroll 0 0 #ffffff;
  border: 1px solid #d8d2b3;
  border-radius: 4px 4px 4px 4px;
  border-style: none;
  color: #818181;
  font-family: "DM Sans", sans-serif;
  font-size: 8px;
  line-height: 1.4em;
  padding: 3px 5px 3px 5px;
  padding: 2px 2px 2px 2px;
}

.prompt-info::-webkit-scrollbar {
  width: 1px;
  /* width of the entire scrollbar */
}

.prompt-info::-webkit-scrollbar-track {
  background: #F7F6F0;
  /* color of the tracking area */
}

.image-info {
  display: flex;
  direction: row;
  padding-top: 5px;
  padding-right: 5px;
}

.cache-img-image,
.cache-img-word {
  width: 22px;
  height: 22px;
  border: 1px solid #d8d2b3;
  background-color: white;
  border-radius: 3px;
  justify-content: center;
  align-items: center;
  margin-right: 4px;
  display: flex;
}

.cache-img-word img {
  max-width: 100%;
  max-height: 100%;
  object-fit: contain;
  // border-radius: 7px;
  justify-content: center;
  align-items: center;
}

.cache-img-image img {
  max-width: 100%;
  max-height: 100%;
  object-fit: contain;
  // border-radius: 7px;
  justify-content: center;
  align-items: center;
}

.option-labels {
  width: 40px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  // margin-bottom: 3px;
}

.option-labels button:not(:last-child) {
  margin-bottom: 3px;
}


.option-label-semantic {
  width: 100%;
  height: 3px;
  border: 1px solid #EDD896;
  background-color: #EDD896;
}

.option-label-color {
  width: 100%;
  height: 3px;
  border: 1px solid #D0EAF6;
  background-color: #D0EAF6;
}

.option-label-shape {
  width: 100%;
  height: 3px;
  border: 1px solid #C1CDF7;
  background-color: #C1CDF7;
}

.gallery-group {
  display: flex;
  width: 300px;
  height: 100%;
  justify-content: space-evenly;
  margin-right: -5px;
  padding-top: 10px;
}

.gallery-item {
  position: relative;
  width: 60px;
  /* adjust width as needed */
  height: 60px;
  border: 1px solid #d8d2b3;
  background-color: white;
  border-radius: 6px;
  display: flex;
  justify-content: center;
  align-items: center;
  // box-shadow: 2px 2px 5px rgba(110, 110, 110, 0.3);
  // margin-right: -10px;
  /* create 10px space between items */
}

.gallery-item img {
  max-width: 100%;
  max-height: 100%;
  object-fit: contain;
  border-radius: 7px;
  justify-content: center;
  align-items: center;
  border: 0px solid #d8d2b3;
}


.gallery-item-button {
  position: absolute;
  top: -8px;
  right: -8px;
  width: 15px;
  height: 15px;
  border-radius: 50%;
  border: 1px solid #bab493;
  background: #ebe6c8;
  outline: none;
  color: #a39d7c;
  padding: 0px;
  cursor: pointer;
  // text-align: center;
  // justify-content: center;
  font-size: 2px;
  // padding-left: 2px;
  // margin-right: -10px;
}
</style>
  