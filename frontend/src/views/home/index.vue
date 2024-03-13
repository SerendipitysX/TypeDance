<template>
  <el-container>
    <el-header v-if="show" style="display: flex;align-items: center;background-color: #EDEFAB;height: 35px;">
      <!-- 171717 -->
      <!-- 导入 -->
      <!-- <import-json></import-json> -->
      &nbsp;
      <import-svg></import-svg>
      &nbsp;
      <import-img></import-img>
      &nbsp;
      <!-- <group></group> -->
      <!-- <lock></lock> -->
      <!-- 对齐方式 -->
      <!-- <align></align> -->
      &nbsp;
      <!-- <flip></flip> -->
      &nbsp;
      <!-- <center-align></center-align> -->
      &nbsp;
      <!-- <group></group> -->
      <!-- &nbsp; -->
      <!-- <zoom></zoom> -->
      &nbsp;
      <!-- <lock></lock> -->
      <!-- &nbsp; -->
      <!-- <dele></dele>
      <clone></clone> -->
      <!-- <flip></flip> -->
      <div style=" float:right;">
        <!-- <zoom></zoom>&nbsp; &nbsp; -->
        <!-- <lang />
        <save></save> -->
        &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 
        &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 
        &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 
        &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 
        &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 
        &nbsp; &nbsp; &nbsp;
        <save></save>
      </div>
    </el-header>
    <el-main style="display: flex; height: calc(100vh - 64px);background-color: #F7F6F0;">
      <div class="left-panel" v-if="show" style="width: 270px;height: 99%;margin-top:12px;">
        <wordView v-if="show"></wordView>
        <!-- <rawData v-if="show"></rawData> -->
        <!-- <theme v-if="show"></theme> -->
        <!-- <textInput v-if="show"></textInput> -->
      </div>

      <!-- 画布区域 -->
      <div style="width: 670px; height: 88%;  margin-left: 3px;margin-top: 2px; overflow: hidden; background:#F7F6F0;">
        <div class="canvas-box">
          <canvas id="canvas"></canvas>
          <div class="canvas-tool"><editAndRefine></editAndRefine></div>
        </div>
        <div class="container-boxes">
          <div class="generate-box" >
            <generate></generate>
          </div>
          <div class="gallery-box">
            <gallery></gallery>
            <!-- <generate></generate>> -->
          </div>
        </div>

      </div>
      <!-- 属性区域 -->
      <!-- <div style="width: 500px; height: 100%; padding-left:10px; overflow-y: auto; background:#F7F6F0">
        <history v-if="show"></history>
        <estimation v-if="show"></estimation>
        <edit v-if="show"></edit>
        <layer v-if="show"></layer>
        <attribute v-if="show"></attribute>
      </div> -->
    </el-main>
  </el-container>
</template>

<script setup>
import { Promotion, EditPen, Operation } from '@element-plus/icons-vue'
// 导入元素
import importJson from '@/components/importJSON.vue'
import importSvg from '@/components/importSvg.vue'
import importImg from '@/components/importImg.vue'

// 顶部组件
import align from '@/components/align.vue'
import centerAlign from '@/components/centerAlign.vue'
import flip from '@/components/flip.vue'
import save from '@/components/save.vue'
import clone from '@/components/clone.vue'
import group from '@/components/group.vue'
import zoom from '@/components/zoom.vue'
import lock from '@/components/lock.vue'
import dele from '@/components/del.vue'
import lang from '@/components/lang.vue'
// 左侧组件
import wordView from '@/components/wordView.vue'
import generate from '@/components/generate.vue'
import gallery from '@/components/gallery.vue'
import editAndRefine from '@/components/editAndRefine.vue'
import toolGallery from '@/components/toolGallery.vue'
import tools from '@/components/tools.vue'
import setSize from '@/components/setSize.vue'

// 右侧组件
import history from '@/components/history.vue'
import layer from '@/components/layer.vue'
import edit from '@/components/edit.vue'
import estimation from '@/components/estimation.vue'

// 功能组件
import EventHandle from '@/utils/eventHandler'
import { fabric } from 'fabric';

// 对齐辅助线
import initAligningGuidelines from '@/core/initAligningGuidelines';
import initControlsRotate from '@/core/initControlsRotate';
import initHotkeys from '@/core/initHotKeys';
import initControls from '@/core/initControls';

//国际化
import { useI18n } from 'vue-i18n'
const { t } = useI18n()

let mSelectMode = ref('') // one | multiple
let mSelectOneType = ref('') // i-text | group...
let mSelectId = ref('')// 选择id
let mSelectIds = ref([])// 选择id

let event = new EventHandle()
let canvas = {}


event.setMaxListeners(50)
provide("canvas", canvas)
provide("fabric", fabric)
provide("event", event)
provide("mSelectMode", mSelectMode)
provide("mSelectOneType", mSelectOneType)
provide("mSelectId", mSelectId)
provide("mSelectIds", mSelectIds)
let menuActive = ref('1')
let show = ref(false)

onMounted(() => {
  event.on('selectOne', (e) => {
    mSelectMode.value = 'one'
    mSelectId.value = e[0].id
    mSelectOneType.value = e[0].type
    mSelectIds.value = e.map(item => item.id)
  })

  event.on('selectMultiple', (e) => {
    mSelectMode.value = 'multiple'
    mSelectId.value = ''
    mSelectIds.value = e.map(item => item.id)
  })

  event.on('selectCancel', () => {
    mSelectId.value = ''
    mSelectIds.value = []
    mSelectMode.value = ''
    mSelectOneType.value = ''
  })

  canvas.c = new fabric.Canvas('canvas');
  canvas = canvas.c
  canvas.set('backgroundColor', '#fff')
  canvas.setWidth(660);
  canvas.setHeight(600);
  canvas.renderAll()

  show.value = true

  windowsLoadEvt(canvas)

  event.init(canvas)
  initAligningGuidelines(canvas)
  initHotkeys(canvas)
  initControls(canvas)
  initControlsRotate(canvas)
})

//获取鼠标坐标
function getMouse(e) {
  var pointer = canvas.getPointer(e.e);
  var posX = Math.floor(pointer.x);
  var posY = Math.floor(pointer.y);
  // console.log(posX + " " + posY);
}

const windowsLoadEvt = (canvas) => {
  canvas.on('mouse:down', (e) => {
    getMouse(e);
  });

  canvas.on('mouse:down', opt => { // 鼠标按下时触发
    let evt = opt.e
    if (evt.altKey === true) { // 是否按住alt
      canvas.selection = false;
      canvas.isDragging = true // isDragging 是自定义的
      canvas.lastPosX = evt.clientX // lastPosX 是自定义的
      canvas.lastPosY = evt.clientY // lastPosY 是自定义的
    }
  })

  canvas.on('mouse:move', opt => { // 鼠标移动时触发
    if (canvas.isDragging) {
      let evt = opt.e
      let vpt = canvas.viewportTransform // 聚焦视图的转换
      vpt[4] += evt.clientX - canvas.lastPosX
      vpt[5] += evt.clientY - canvas.lastPosY
      canvas.requestRenderAll()
      canvas.lastPosX = evt.clientX
      canvas.lastPosY = evt.clientY
    }
  })

  canvas.on('mouse:up', opt => { // 鼠标松开时触发
    canvas.setViewportTransform(canvas.viewportTransform) // 设置此画布实例的视口转换  
    canvas.isDragging = false
  })

  canvas.on('mouse:wheel', opt => {
    let delta = opt.e.deltaY // 滚轮，向上滚一下是 -100，向下滚一下是 100
    let zoom = canvas.getZoom() // 获取画布当前缩放值
    zoom *= 0.999 ** delta
    if (zoom > 5) zoom = 5
    if (zoom < 0.5) zoom = 0.5
    canvas.zoomToPoint({ // 关键点
      x: opt.e.offsetX,
      y: opt.e.offsetY
    },
      zoom
    )
    opt.e.preventDefault()
    opt.e.stopPropagation()
  })
}


</script>
<style lang="less" scoped>
:deep(.el-header) {
  padding: 0 10px;
  background: #515a6e;
  height: 64px;
  line-height: 64px;
}

.el-main {
  --el-main-padding: 0px;
}

.home,
.el-container {
  height: 96vh;
}

.icon {
  display: block;
}

.container-boxes {
  display: flex;
}


.canvas-box {
  overflow: hidden;
  display: flex;
  position: relative;
  width: 99%;
  margin: 0px 5px 0px 2px;
  height: 62.5%;
  // height: 59%;
  background-color: white;
}

.canvas-tool {
  position: absolute;
  top: 0px;
  left: 520px;
  z-index: 1;
  width: 1;
}

.container-boxes {
  display: flex;
  // overflow: hidden;
  width: 99%;
  margin: 5px 5px 0px 2px;
  height: 32.5%;
  // height: 36%;
  // background-color: white;
}

#canvas {
  margin: 0 auto;
}

.content {
  flex: 1;
  width: 200px;
  padding: 10px;
  padding-top: 0;
  height: 95%;
  overflow-y: auto;
}

// .refs {
//   border: 1.5px #565656 dashed;
//   border-radius: 7px;
//   // background-color: orange;
//   // color: orange;
// }
</style>
