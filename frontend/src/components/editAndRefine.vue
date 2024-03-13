<!--
 * @Author: 秦少卫
 * @Date: 2022-09-03 19:16:55
 * @LastEditors: 秦少卫
 * @LastEditTime: 2022-09-06 23:20:40
 * @Description: 图层面板
-->

<template>
    <div class="editAndPreview">
        <div class="tool-container">
            <button class="tool-btn" id="big" @click="big">
                <svg t="1692515725386" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg"
                    p-id="2282">
                    <path
                        d="M768 448a320 320 0 1 0-320 320 320 320 0 0 0 320-320z m64 0A384 384 0 1 1 448 64a384 384 0 0 1 384 384z"
                        p-id="2283"></path>
                    <path
                        d="M681.28 726.72a32 32 0 0 1 45.44-45.44l160 160a32 32 0 0 1-45.44 45.44zM320 480a32 32 0 0 1 0-64h256a32 32 0 0 1 0 64z"
                        p-id="2284"></path>
                    <path d="M480 576a32 32 0 0 1-64 0V320a32 32 0 0 1 64 0z" p-id="2285"></path>
                </svg>
            </button>
            <button class="tool-btn" id="small" @click="small">
                <svg t="1692515787856" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg"
                    p-id="1686">
                    <path
                        d="M768 448a320 320 0 1 0-320 320 320 320 0 0 0 320-320z m64 0A384 384 0 1 1 448 64a384 384 0 0 1 384 384z"
                        p-id="1687"></path>
                    <path
                        d="M681.28 726.72a32 32 0 0 1 45.44-45.44l160 160a32 32 0 0 1-45.44 45.44zM288 480a32 32 0 0 1 0-64h320a32 32 0 0 1 0 64z"
                        p-id="1688"></path>
                </svg>
            </button>
            <button class="tool-btn" id="copy" @click="clone">
                <svg t="1692515636828" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg"
                    p-id="14053">
                    <path
                        d="M838.4 68.266667h-512c-46.933333 0-85.333333 36.266667-85.333333 81.066666v38.4H185.6c-46.933333 0-85.333333 38.4-85.333333 85.333334v597.333333c0 46.933333 38.4 85.333333 85.333333 85.333333h512c46.933333 0 85.333333-38.4 85.333333-85.333333v-36.266667h55.466667c46.933333 0 85.333333-38.4 85.333333-85.333333v-597.333333c0-44.8-38.4-83.2-85.333333-83.2z m-98.133333 802.133333c0 23.466667-19.2 42.666667-42.666667 42.666667h-512c-23.466667 0-42.666667-19.2-42.666667-42.666667v-597.333333c0-23.466667 19.2-42.666667 42.666667-42.666667h512c23.466667 0 42.666667 19.2 42.666667 42.666667v597.333333z m140.8-119.466667c0 23.466667-19.2 42.666667-42.666667 42.666667h-55.466667V273.066667c0-46.933333-38.4-85.333333-85.333333-85.333334H283.733333V149.333333c0-21.333333 19.2-38.4 42.666667-38.4h512c23.466667 0 42.666667 19.2 42.666667 42.666667v597.333333z m-450.133334-83.2h-204.8c-12.8 0-21.333333 8.533333-21.333333 21.333334s8.533333 21.333333 21.333333 21.333333h204.8c12.8 0 21.333333-8.533333 21.333334-21.333333s-10.666667-21.333333-21.333334-21.333334z m98.133334-10.666666c-17.066667 0-32 14.933333-32 32s14.933333 32 32 32 32-14.933333 32-32-12.8-32-32-32z m128-234.666667H224c-12.8 0-21.333333 8.533333-21.333333 21.333333s8.533333 21.333333 21.333333 21.333334h433.066667c12.8 0 21.333333-8.533333 21.333333-21.333334s-8.533333-21.333333-21.333333-21.333333z"
                        p-id="14054"></path>
                </svg>
            </button>
            <button class="tool-btn" id="del" @click="del">
                <svg t="1692515467613" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg"
                    p-id="9241">
                    <path d="M663 361.6h51.2v440.6H663z" p-id="9242"></path>
                    <path
                        d="M772.3 219.5c0.5-4.5 0.8-9 0.8-13.4v-18.4c0-68.1-55.4-123.5-123.5-123.5H374.2c-68.1 0-123.5 55.4-123.5 123.5v18.4c0 4.5 0.3 9 0.8 13.4H71.2v51.2h102.5v607.8c0 44.7 36.4 81 81 81h514.1c44.7 0 81-36.4 81-81V270.7h102.6v-51.2H772.3z m-467.4-13.4v-18.4c0-38.2 31.1-69.2 69.3-69.2h275.4c38.2 0 69.3 31.1 69.3 69.2v18.4c0 4.5-0.5 9-1.4 13.4H304.8l1.3-0.3c-0.8-4.2-1.2-8.7-1.2-13.1zM798 878.5c0 16.1-13.1 29.1-29.1 29.1H254.8c-16.1 0-29.1-13.1-29.1-29.1V270.7H798v607.8z"
                        p-id="9243"></path>
                    <path d="M484 361.6h51.2v440.6H484zM305 361.6h51.2v440.6H305z" p-id="9244"></path>
                </svg>
            </button>
            <button class="tool-btn" id="group" :disabled="!isMultiple" @click="group">
                <svg t="1692515134810" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg"
                    p-id="5647">
                    <path
                        d="M637.013333 298.666667l0 128-341.333333 0L295.68 298.666667 637.013333 298.666667M637.013333 256l-341.333333 0c-23.552 0-42.666667 19.072-42.666667 42.666667l0 128c0 23.594667 19.114667 42.666667 42.666667 42.666667l341.333333 0c23.594667 0 42.666667-19.072 42.666667-42.666667L679.68 298.666667C679.68 275.072 660.565333 256 637.013333 256L637.013333 256zM722.346667 554.666667l0 128-341.333333 0 0-128L722.346667 554.666667M722.346667 512l-341.333333 0c-23.552 0-42.666667 19.072-42.666667 42.666667l0 128c0 23.594667 19.114667 42.666667 42.666667 42.666667l341.333333 0c23.594667 0 42.666667-19.072 42.666667-42.666667l0-128C765.013333 531.072 745.898667 512 722.346667 512L722.346667 512zM167.68 128l0 42.666667-42.666667 0L125.013333 128 167.68 128M210.346667 85.333333l-128 0 0 128 128 0L210.346667 85.333333 210.346667 85.333333zM167.68 810.666667l0 42.666667-42.666667 0 0-42.666667L167.68 810.666667M210.346667 768l-128 0 0 128 128 0L210.346667 768 210.346667 768zM893.013333 810.666667l0 42.666667-42.666667 0 0-42.666667L893.013333 810.666667M935.68 768l-128 0 0 128 128 0L935.68 768 935.68 768zM893.013333 128l0 42.666667-42.666667 0L850.346667 128 893.013333 128M935.68 85.333333l-128 0 0 128 128 0L935.68 85.333333 935.68 85.333333zM807.68 128l-640 0 0 42.666667 640 0L807.68 128zM807.68 810.666667l-640 0 0 42.666667 640 0L807.68 810.666667zM167.68 810.666667 167.68 213.333333l-42.666667 0 0 597.333333L167.68 810.666667zM893.013333 810.666667 893.013333 213.333333l-42.666667 0 0 597.333333L893.013333 810.666667z"
                        p-id="5648"></path>
                </svg>
            </button>
            <button class="tool-btn" id="ungroup" :disabled="!isGroup" @click="unGroup">
                <svg t="1692515169213" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg"
                    p-id="5795">
                    <path
                        d="M170.666667 128l0 42.666667L128 170.666667 128 128 170.666667 128M213.333333 85.333333 85.333333 85.333333l0 128 128 0L213.333333 85.333333 213.333333 85.333333zM170.666667 640l0 42.666667L128 682.666667l0-42.666667L170.666667 640M213.333333 597.333333 85.333333 597.333333l0 128 128 0L213.333333 597.333333 213.333333 597.333333zM725.333333 640l0 42.666667-42.666667 0 0-42.666667L725.333333 640M768 597.333333l-128 0 0 128 128 0L768 597.333333 768 597.333333zM725.333333 128l0 42.666667-42.666667 0L682.666667 128 725.333333 128M768 85.333333l-128 0 0 128 128 0L768 85.333333 768 85.333333zM640 128 170.666667 128l0 42.666667 469.333333 0L640 128zM640 640 170.666667 640l0 42.666667 469.333333 0L640 640zM170.666667 640 170.666667 213.333333 128 213.333333l0 426.666667L170.666667 640zM725.333333 640 725.333333 213.333333l-42.666667 0 0 426.666667L725.333333 640zM341.333333 853.333333l0 42.666667L298.666667 896l0-42.666667L341.333333 853.333333M384 810.666667 256 810.666667l0 128 128 0L384 810.666667 384 810.666667zM896 853.333333l0 42.666667-42.666667 0 0-42.666667L896 853.333333M938.666667 810.666667l-128 0 0 128 128 0L938.666667 810.666667 938.666667 810.666667zM896 341.333333l0 42.666667-42.666667 0L853.333333 341.333333 896 341.333333M938.666667 298.666667l-128 0 0 128 128 0L938.666667 298.666667 938.666667 298.666667zM810.666667 341.333333l-85.333333 0 0 42.666667 85.333333 0L810.666667 341.333333zM810.666667 853.333333 341.333333 853.333333l0 42.666667 469.333333 0L810.666667 853.333333zM341.333333 853.333333l0-170.666667L298.666667 682.666667l0 170.666667L341.333333 853.333333zM896 853.333333 896 426.666667l-42.666667 0 0 426.666667L896 853.333333zM554.666667 341.333333l0 85.333333L298.666667 426.666667 298.666667 341.333333 554.666667 341.333333M554.666667 298.666667 298.666667 298.666667C275.072 298.666667 256 317.738667 256 341.333333l0 85.333333c0 23.594667 19.072 42.666667 42.666667 42.666667l256 0c23.594667 0 42.666667-19.072 42.666667-42.666667L597.333333 341.333333C597.333333 317.738667 578.261333 298.666667 554.666667 298.666667L554.666667 298.666667z"
                        p-id="5796"></path>
                </svg>
            </button>
            <button class="tool-btn" id="color-selection">
                <input type="color" id="color-picker" />
                <svg t="1692514338024" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg"
                    p-id="4455">
                    <path
                        d="M954.756963 291.473421c-3.610224-3.684926-8.04114-5.583159-13.167904-5.641487-12.515035-0.141216-26.508747 10.942213-36.035728 20.255323L564.640917 637.263935c-12.500709 12.228509-58.515718 86.965677-60.468187 90.143043l-7.451716 12.121062 12.135388-7.42818c3.217275-1.967818 78.963423-48.373731 91.437525-60.569494l340.91139-331.177702C956.35639 325.537238 967.876772 304.916595 954.756963 291.473421L954.756963 291.473421z"
                        p-id="4456"></path>
                    <path
                        d="M741.987045 394.4784c0 27.608801-22.407336 50.015114-50.015114 50.015114-27.612894 0-50.021254-22.406313-50.021254-50.015114 0-27.609825 22.408359-50.018184 50.021254-50.018184C719.579709 344.460216 741.987045 366.868575 741.987045 394.4784L741.987045 394.4784z"
                        p-id="4457"></path>
                    <path
                        d="M216.811977 569.531298c-27.609825 0-50.016137-22.403243-50.016137-50.012044 0-27.611871 22.406313-50.02023 50.016137-50.02023 27.607778 0 50.01716 22.408359 50.01716 50.02023C266.829138 547.128055 244.419755 569.531298 216.811977 569.531298L216.811977 569.531298z"
                        p-id="4458"></path>
                    <path
                        d="M291.837718 394.4784c0-27.609825 22.408359-50.018184 50.015114-50.018184 27.609825 0 50.018184 22.408359 50.018184 50.018184 0 27.608801-22.407336 50.015114-50.018184 50.015114C314.244031 444.493513 291.837718 422.11176 291.837718 394.4784L291.837718 394.4784z"
                        p-id="4459"></path>
                    <path
                        d="M466.895733 344.460216c0-27.608801 22.406313-50.015114 50.015114-50.015114 27.611871 0 50.019207 22.406313 50.019207 50.015114 0 27.608801-22.408359 50.018184-50.019207 50.018184C489.302045 394.4784 466.895733 372.093577 466.895733 344.460216L466.895733 344.460216z"
                        p-id="4460"></path>
                    <path
                        d="M853.740268 514.084475c-22.988574 148.966777-158.732188 299.942303-351.946724 299.942303-36.781718 0-75.998905-7.274684-107.597577-19.958564-33.607422-13.490246-48.850591-29.353538-51.907207-39.693024-1.594311-5.39794-3.092431-11.296277-4.679579-17.541515-4.649903-18.301831-9.921977-39.045271-20.252253-56.259328-18.375509-30.618345-44.814672-37.044708-63.760163-37.044708-7.166213 0-14.798031 0.913812-22.675442 2.711761-12.865006 2.935865-25.362644 4.423753-37.140898 4.423753-25.12319 0-67.463508-6.664793-68.765153-51.307549-6.590092-227.942479 180.734294-351.748203 369.297904-373.325637 13.33675-1.524726 27.602661-2.296299 42.402739-2.296299 53.123918 0 111.543446 10.000771 152.463414 26.099425 9.247618 3.637854 14.375405 6.016017 39.203884 18.184151 25.653263 12.570293 46.347584 30.432103 62.897515 47.642067l30.157857-53.074799c-18.026562-17.013489-40.333614-34.406624-67.102281-47.52541-24.889877-12.196787-31.893384-15.514345-43.565215-20.10592-47.339168-18.62315-114.03315-30.193673-174.053128-30.193673-17.026792 0-33.545 0.900509-49.102325 2.677992-115.513874 13.220093-220.687238 59.057047-296.142767 129.074727-85.507466 79.342046-128.872113 184.653557-125.405151 304.555367 1.004887 34.470069 15.117302 63.017242 40.810474 82.556251 22.38073 17.019629 52.43114 26.01449 86.903256 26.01449 16.186657 0 33.096792-1.985214 50.26787-5.903453 3.581572-0.817622 6.79373-1.232061 9.54847-1.232061 11.469216 0 16.989953 10.04375 26.852578 48.853661 1.653663 6.509251 3.364631 13.240559 5.281283 19.730367 9.43386 31.911804 39.343053 58.783825 86.494956 77.710896 38.318724 15.382339 85.544305 24.203238 129.566938 24.203238 54.104245 0 106.473987-10.134825 155.659199-30.123065 46.24116-18.793018 88.50166-45.763276 125.606743-80.164784 35.744086-33.140795 65.270563-71.79107 87.756693-114.883517 22.526039-43.163055 36.888142-88.666412 42.691311-135.2688 0.261966-2.117221 0.508583-4.321422 0.731664-6.548136l0.148379-1.469468 0-0.057305c0.222057-2.336208 0.404206-4.694929 0.571005-7.064906L853.740268 514.084475 853.740268 514.084475z"
                        p-id="4461">
                    </path>
                </svg>
            </button>
            <button class="tool-btn" id="convert-to-svg" @click="convertTosvg">
                <svg t="1692514482304" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg"
                    p-id="5636">
                    <path
                        d="M759.466667 755.456H581.8368c-14.421333 0-26.112 12.475733-26.112 27.869867v168.618666h28.433067L759.466667 760.439467v-4.983467zM759.466667 699.733333v-88.183466c0-15.189333 11.4688-27.477333 25.6-27.477334s25.6 12.288 25.6 27.477334v160.136533c0 7.2192-2.645333 14.1312-7.338667 19.285333L613.154133 998.7072a24.746667 24.746667 0 0 1-18.261333 8.226133H211.626667C146.602667 1006.933333 93.866667 950.306133 93.866667 880.452267V143.530667C93.866667 73.693867 146.602667 17.066667 211.626667 17.066667h481.28C757.930667 17.066667 810.666667 73.693867 810.666667 143.547733v48.930134c0 15.189333-11.4688 27.477333-25.6 27.477333s-25.6-12.288-25.6-27.477333V143.530667c0-39.4752-29.7984-71.492267-66.56-71.492267H211.626667c-36.7616 0-66.56 32.017067-66.56 71.509333v736.887467c0 39.4752 29.7984 71.492267 66.56 71.492267H503.466667v-168.618667C503.466667 737.160533 538.555733 699.733333 581.8368 699.733333H759.466667zM348.996267 273.066667c28.7744 0 50.210133 5.819733 63.880533 17.8176 14.557867 12.680533 20.462933 32.546133 17.442133 59.272533h-39.765333c-0.341333-15.069867-4.642133-26.043733-12.219733-32.546133-7.509333-6.8608-20.599467-9.9328-38.417067-9.9328-15.428267 0-27.477333 2.048-36.608 6.5024-11.332267 5.137067-17.8688 13.704533-20.224 25.361066-2.082133 10.274133 1.655467 18.8416 12.049067 25.002667 4.590933 2.730667 17.578667 7.8848 38.741333 15.086933 31.163733 10.274133 50.7392 18.500267 59.221333 23.978667 18.653867 12.680533 25.736533 30.139733 21.162667 52.753067-4.4544 21.930667-16.571733 39.424-36.266667 52.087466-19.626667 12.3392-45.294933 18.8416-76.458666 18.8416-30.1568 0-52.616533-5.819733-67.037867-17.476266-17.646933-14.3872-24.3712-37.000533-19.746133-68.181334h39.7312c-1.006933 18.500267 2.798933 31.863467 11.810133 39.748267 8.209067 6.8608 22.186667 10.615467 42.3936 10.615467 17.8176 0 32.836267-3.072 44.288-8.9088 11.537067-6.161067 18.602667-14.045867 20.701867-24.32 2.645333-13.021867-3.157333-23.296-16.708267-30.839467-4.3008-2.389333-18.944-7.8848-44.356267-16.093867-28.194133-9.591467-45.653333-16.452267-52.0192-20.565333-16.554667-11.298133-22.459733-27.7504-18.090666-49.322667 4.386133-21.6064 16.776533-38.741333 37.768533-51.063466C299.861333 278.869333 322.594133 273.066667 349.013333 273.066667z m122.504533 4.795733h43.52l26.692267 199.406933h1.024l107.6224-199.406933h43.52l-136.669867 244.6336h-48.298667l-37.410133-244.6336zM827.938133 273.066667c31.522133 0 54.801067 6.8608 70.109867 20.906666 14.6944 13.704533 21.5552 33.911467 20.445867 61.320534H878.08c-0.238933-15.752533-5.410133-27.409067-14.779733-35.293867-9.710933-7.867733-24.0128-11.639467-42.513067-11.639467-22.954667 0-42.6496 7.5264-59.221333 23.296-18.056533 16.452267-29.9008 39.406933-36.010667 69.546667-5.853867 28.791467-3.857067 51.063467 6.024533 66.474667 10.717867 16.452267 30.976 24.661333 60.791467 24.661333 11.639467 0 22.869333-1.365333 33.723733-4.096a140.424533 140.424533 0 0 0 28.672-11.3152l10.222934-50.363733h-64.768l6.9632-34.269867h104.840533l-20.992 103.4752a180.0192 180.0192 0 0 1-49.271467 23.296c-18.926933 5.495467-39.0144 8.226133-60.928 8.226133-39.082667 0-66.730667-12.3392-83.3024-37.000533-15.5648-22.954667-19.456-52.770133-12.0832-89.088 7.441067-36.6592 23.5008-66.798933 48.503467-90.453333C760.337067 285.405867 791.637333 273.066667 827.938133 273.066667z"
                        p-id="5637"></path>
                </svg>
            </button>
        </div>

        <div class="refine">
            <div class="evaluation-img">
                <img id="evaluation-img-self" src="/src/assets/evaluation/default.png" data-alt="">
                <div class="eva-score-box">
                    <button class="eva-score" id="eva-score">-</button>
                </div>
            </div>

            <div class="refine-slider">
                <span class="slider-description">
                    <svg t="1693117424039" class="icon" viewBox="0 0 1024 1024" version="1.1"
                        xmlns="http://www.w3.org/2000/svg" p-id="4209">
                        <path
                            d="M853.333333 170.666667H170.666667a42.666667 42.666667 0 0 0-42.666667 42.666666v128a42.666667 42.666667 0 0 0 85.333333 0V256h256v554.666667H384a42.666667 42.666667 0 0 0 0 85.333333h256a42.666667 42.666667 0 0 0 0-85.333333h-85.333333V256h256v85.333333a42.666667 42.666667 0 0 0 85.333333 0V213.333333a42.666667 42.666667 0 0 0-42.666667-42.666666z"
                            p-id="4210"></path>
                    </svg> </span>
                <input type="range" id="control-evaluation" name="control-evaluation" min="-1" max="1" value="0"
                    step="0.05">
                <span class="slider-description">
                    <svg t="1693105885438" class="icon" viewBox="0 0 1024 1024" version="1.1"
                        xmlns="http://www.w3.org/2000/svg" p-id="8384">
                        <path
                            d="M256 298.666667a85.333333 85.333333 0 1 1 85.333333 85.333333 85.333333 85.333333 0 0 1-85.333333-85.333333z m674.133333 415.146666l-256-341.333333a32.426667 32.426667 0 0 0-51.2 0l-170.666666 220.586667a21.333333 21.333333 0 0 1-33.28 0l-93.44-113.493334a32 32 0 0 0-49.92 0l-181.333334 234.24a42.666667 42.666667 0 0 0-8.96 26.026667v38.826667a32.426667 32.426667 0 0 0 32 32h789.333334a32.426667 32.426667 0 0 0 32-32v-39.253334a42.666667 42.666667 0 0 0-8.533334-25.6z"
                            p-id="8385"></path>
                    </svg>
                </span>
            </div>

            <!-- <div class="evaluation-options">
                <button class="inline-button" @click="displayText" style="width: 90px; margin-right: 2px;">Evaluate</button>
                <span class="range-slider__value"> 0.75
                </span>
                <button class="inline-button" id="confirmButton" style="width: 30px;" @click="displayTextOnCanvas">
                    <svg t="1690350488185" class="icon-function" viewBox="0 0 1024 1024" version="1.1"
                        xmlns="http://www.w3.org/2000/svg" p-id="37475">
                        <path
                            d="M346.595344 684.495656 135.774825 473.675136l-71.492264 71.447239 282.312784 282.268782 606.406137-606.358041-71.447239-71.492264L346.595344 684.495656z"
                            p-id="37476"></path>
                    </svg>
                </button>
            </div> -->
            <div class="evaluation-options">
                <button class="inline-button" @click="clickEvaluate"
                    style="width: 90px; margin-right: 4px;">Evaluate</button>
                <button class="inline-button" id="confirmButton" @click="displayTextOnCanvas">
                    <svg t="1690350488185" class="icon-function" viewBox="0 0 1024 1024" version="1.1"
                        xmlns="http://www.w3.org/2000/svg" p-id="37475">
                        <path
                            d="M346.595344 684.495656 135.774825 473.675136l-71.492264 71.447239 282.312784 282.268782 606.406137-606.358041-71.447239-71.492264L346.595344 684.495656z"
                            p-id="37476"></path>
                    </svg>
                </button>
            </div>

            <!-- <el-button-group v-show="mSelectMode === 'one'" size="small">
      <el-button @click="up"><span v-html="btnIconType('up')"></span></el-button>
      <el-button @click="down"><span v-html="btnIconType('down')"></span></el-button>
    </el-button-group> -->
            <!-- <button @click="up"> 123</button> -->
        </div>
    </div>
</template>
  
<script setup>
import { useI18n } from 'vue-i18n'
import { ref, toDisplayString } from 'vue';
import { v4 as uuid } from 'uuid';
import mitt from 'mitt';
import { useDesignPriorStore } from '../store/modules/imageViewStore'
import { useGenerateStore } from '../store/modules/generateStore';
import { ConvertToSvg, startEvaluate, startRefine } from '../service/dataService';
import layer from '@/components/layer.vue'

const storeDesignPrior = useDesignPriorStore()
const storeGenerate = useGenerateStore()
const eventBus = inject("eventBus")
let labelImageList = ref([])
let generationStateDict = ref({})
let semanticPrompt = ref("")
let wrapSvg = ref("")
const canvas = inject("canvas")
let anchorEvaScore = ref(0)
let evaResultScore = ref(10)
let dataAlt = ref("")

const big = () => {
    let zoomRatio = canvas.c.getZoom();
    zoomRatio += 0.05;
    canvas.c.zoomToPoint(
        new fabric.Point(canvas.c.getWidth() / 2, canvas.c.getHeight() / 2),
        zoomRatio,
    )
    zoom.value = `${Math.round(zoomRatio * 100)}%`
}

const small = () => {
    let zoomRatio = canvas.c.getZoom();
    zoomRatio -= 0.05;
    canvas.c.zoomToPoint(
        new fabric.Point(canvas.c.getWidth() / 2, canvas.c.getHeight() / 2),
        zoomRatio,
    )
    zoom.value = `${Math.round(zoomRatio * 100)}%`
}

const clone = () => {
    const activeObject = canvas.c.getActiveObject();
    activeObject.clone(cloned => {
        canvas.c.discardActiveObject()
        // 间距设置
        const grid = 10
        cloned.set({
            left: cloned.left + grid,
            top: cloned.top + grid,
        })
        canvas.c.add(cloned)
        canvas.c.setActiveObject(cloned);
        canvas.c.requestRenderAll();
    })
}

const del = () => {
    const activeObject = canvas.c.getActiveObjects();
    activeObject && activeObject.map(item => canvas.c.remove(item))
    canvas.c.requestRenderAll()
    canvas.c.discardActiveObject()
}

let mSelectMode = inject('mSelectMode')
let mSelectOneType = inject('mSelectOneType')
// 单选且等于组元素
const isGroup = computed(() => {
    return (mSelectMode.value === 'one' && mSelectOneType.value === 'group')
})

// 是否为多选
const isMultiple = computed(() => {
    return (mSelectMode.value === 'multiple')
})
// // 拆分组
const unGroup = () => {
    // 先获取当前选中的对象，然后打散
    canvas.c.getActiveObject().toActiveSelection()
    canvas.c.getActiveObject().getObjects().forEach(item => {
        item.set('id', uuid())
    })
    canvas.c.discardActiveObject().renderAll();
}
const group = () => {
    // 组合元素
    var activeObj = canvas.c.getActiveObject();
    var activegroup = activeObj.toGroup();
    var objectsInGroup = activegroup.getObjects();
    activegroup.clone((newgroup) => {
        canvas.c.remove(activegroup);
        objectsInGroup.forEach((object) => {
            canvas.c.remove(object);
        });
        canvas.c.add(newgroup);
        canvas.c.setActiveObject(newgroup);
    });
}

function convertTosvg() {
    var activeObj = canvas.c.getActiveObject();
    localStorage.setItem('activeObj', JSON.stringify(activeObj));
    var dataURL = JSON.parse(localStorage.getItem('activeObj'));
    let param = {
        data: dataURL
    };
    ConvertToSvg(param, function (data) {
        fabric.loadSVGFromURL('/src/assets/canvas/image.svg', function (objects, options) {
            var svgObject = fabric.util.groupSVGElements(objects, options);
            svgObject.id = "image";
            canvas.c.add(svgObject);
            canvas.c.setActiveObject(svgObject);
        });
    })
}

function clickEvaluate() {
    var activeObj = canvas.c.getActiveObject();
    localStorage.setItem('activeObj', JSON.stringify(activeObj));
    var dataURL = JSON.parse(localStorage.getItem('activeObj'));
    // get alt(prompt)
    const alt = activeObj.get('name');
    // load image
    const evaImg = document.getElementById("evaluation-img-self")
    evaImg.src = dataURL.src
    // evaImg.setAttribute("data-alt", alt)
    dataAlt.value = alt;
    let param = { "data": dataURL.src, "alt": alt }
    startEvaluate(param, function (data) {
        // load score
        evaResultScore.value = data.result_score
        var rangeValue = document.getElementById("eva-score");
        var slider = document.getElementById("control-evaluation");
        rangeValue.textContent = Math.abs(data.result_score);
        slider.value = data.result_score;
        anchorEvaScore.value = data.result_score;

        if (slider.value < 0) {
            rangeValue.style.backgroundColor = "rgba(203, 82, 40, 0.4)";
            rangeValue.style.color = "rgba(185, 82, 48, 1)";
        }
        if (slider.value > 0) {
            rangeValue.style.backgroundColor = "rgba(38, 111, 136, 0.4)";
            rangeValue.style.color = "rgba(38, 111, 136, 1)";
        }
        if (slider.value == 0) {
            rangeValue.style.backgroundColor = "rgba(225, 230, 96, 0.5)";
            rangeValue.style.color = "#797B0B";
        }

    })
}

function displayTextOnCanvas() {
    const evaImg = document.getElementById("evaluation-img-self")
    const imgEl = document.createElement('img');
    imgEl.src = evaImg.src
    // 插入页面
    document.body.appendChild(imgEl);
    imgEl.onload = () => {
        // 创建图片对象
        const imgInstance = new fabric.Image(imgEl, {
            id: uuid(),
            left: 100, top: 100,
        });
        // 设置缩放
        imgInstance.scale(0.5);
        canvas.c.add(imgInstance)
        canvas.c.setActiveObject(imgInstance);
        canvas.c.renderAll()
        // 删除页面中的图片元素
        imgEl.remove()
    }
}

onMounted(() => {
    const colorSelection = document.getElementById('color-selection');
    const colorPicker = document.getElementById('color-picker');
    const icon = document.querySelector('#color-selection .icon');

    icon.addEventListener('click', function () {
        colorPicker.click();
    });
    // Event listener for color picker change
    colorPicker.addEventListener('change', function () {
        // Get the selected color value
        var selectedColor = colorPicker.value;

        // Get the active object on the canvas
        var activeObject = canvas.c.getActiveObject();

        // Check if an object is selected
        if (activeObject) {
            // Set the fill color of the selected object
            activeObject.set('fill', selectedColor);
            // Render the canvas to reflect the color change
            canvas.c.renderAll();
        }
    });

    // evaluation
    var slider = document.getElementById("control-evaluation");
    var rangeValue = document.getElementById("eva-score");

    slider.addEventListener("mouseup", function () {
        // score 变化
        // change color
        if (slider.value < 0) {
            rangeValue.style.backgroundColor = "rgba(203, 82, 40, 0.4)";
            rangeValue.style.color = "rgba(185, 82, 48, 1)";
        }
        if (slider.value > 0) {
            rangeValue.style.backgroundColor = "rgba(38, 111, 136, 0.4)";
            rangeValue.style.color = "rgba(38, 111, 136, 1)";
        }
        if (slider.value == 0) {
            rangeValue.style.backgroundColor = "rgba(225, 230, 96, 0.5)";
            rangeValue.style.color = "#797B0B";
        }
        rangeValue.textContent = Math.abs(slider.value);
        // image 变化
        if (evaResultScore.value != 10) { //说明是有evaluate过的
            let param = { "value": slider.value, "anchor": evaResultScore.value, "alt": dataAlt.value }
            startRefine(param, function (data) {
                const evaImg = document.getElementById("evaluation-img-self");
                evaImg.src = data.dataURL;
            });
        }
    });

})


</script>
  

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="less">
.editAndPreview {
    display: flex;
    flex-direction: column;
    // background-color: rgba(216, 210, 179, 0.1);
    width: 140px;
    height: 568px;
    align-items: flex-end;
}

.tool-container {
    display: flex;
    flex-direction: column;
    // justify-content: flex-end;
    align-items: flex-end;
    margin-right: 6px
}

.tool-container:not(:last-child) {
    margin-bottom: 4px;
}

.tool-container>*:first-child {
    margin-top: 10px;
}

.tool-btn {
    background-color: rgba(216, 210, 179, 0.3);
    width: 30px;
    height: 30px;
    border: none;
    border-radius: 5px;
    color: white;
    padding: 4px 4px;
    font-size: 18px;
    cursor: pointer;
    margin-bottom: 5px;
}

.tool-btn>.icon path {
    //   fill: #797B0B;
    // stroke: 10px;
    fill: #6c6952;
}

input[type="color"] {
    border: none;
    background-color: transparent;
    width: 30px;
    height: 30px;
    outline: none;
}

#color-picker::-webkit-color-swatch {
    border-radius: 100%;
}

#color-picker {
    //    display: none;
    // visibility: hidden;
    opacity: 0;
}

#color-picker::-webkit-color-swatch-wrapper {
    transform-origin: right top;
}

#color-selection {
    position: relative;
}

#color-selection .icon {
    position: absolute;
    top: 5px;
    left: 5px;
    //   width: 100%;
    //   height: 100%;
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}

.refine {
    display: flex;
    flex-direction: column;
    background-color: rgba(216, 210, 179, 0.1);
    width: 124px;
    height: 160px;
    border-radius: 10px;
    margin-bottom: 5px;
    // border: 1px solid rgb(230, 231, 188);
    justify-content: center;
    align-items: center;
    margin-right: 6px
}

.evaluation-img {
    display: flex;
    width: 108px;
    height: 108px;
    border-radius: 8px;
    justify-content: center;
    align-items: center;
    border: 1.5px solid #d8d2b3;
    // margin-bottom: 5px;
}

.evaluation-img img {
    width: 100px;
    height: 100px;
    border-radius: 8px;
    justify-content: center;
    align-items: center;
    object-fit: contain; // 不改变图片比例且完整显示
    // border: 1.5px solid #d8d2b3;
    // margin-bottom: 5px;
}

.evaluation-options {
    display: flex;
    align-items: center;
    justify-content: space-between;
    width: 86%;
    // margin-left: 2px;
}

.inline-button {
    display: inline-block;
    background-color: #EDEFAB;
    // background-color: #e6e0bc;
    width: 68px;
    height: 20px;
    border-radius: 4px;
    text-align: center;
    border: 0px;
    font-size: 10px;
    color: #797B0B;
    // color: #7b700b;
    line-height: 2px;
    cursor: pointer;
}

.inline-button>.icon-function path {
    fill: #797B0B;
}

.icon-function {
    width: 12px;
    height: 12px
}

// slider
.refine-slider {
    display: flex;
    width: 88%;
    align-items: center;
    justify-content: center;
    //   margin-bottom: 4px;
}

@media screen and (-webkit-min-device-pixel-ratio:0) {
    input[type='range'] {
        overflow: hidden; // 非常关键
        width: 100%;
        height: 6px;
        -webkit-appearance: none;
        // background-color: #e6e0bc;
        // background: linear-gradient(45deg,
        //         #7A270B 0%,
        //         #FEFCDC 50%,
        //         #024D4F 100%);
        // background: linear-gradient(45deg,
        //         #F2BBB7 0%,
        //         #FEFCDC 50%,
        //         #D1F4EE 100%);
        background: linear-gradient(45deg,
                #B95230 0%,
                #FEFCDC 50%,
                #266F88 100%);
        border-radius: 8px;
        // margin-bottom: 6px;
    }

    input[type='range']::-webkit-slider-thumb {
        -webkit-appearance: none;
        width: 6px;
        height: 6px;
        border-radius: 10px;
        cursor: pointer;
        background: #797B0B; //797B0B
        // box-shadow: -80px 0 0 80px #EDEFAB;
    }

}

.slider-description {
    display: inline-block;
    position: relative;
    line-height: 8px;
    text-align: center;
    border-radius: 3px;
    align-items: center;
    justify-content: center;
}

.slider-description .icon {
    width: 10px;
}

.slider-description>.icon path {
    fill: #797B0B;
}

.slider-description .icon-text {
    width: 10px;
}

.slider-description>.icon-text path {
    fill: #B95230;
}

.slider-description .icon-img {
    width: 10px;
}

.slider-description>.icon-img path {
    fill: #266F88;
}

.eva-score-box {
    position: absolute;
    top: 382px;
    left: 87px;
    z-index: 1;
    width: 1;
}

.eva-score {
    // width: 34px;
    // height: 34px;
    // border-radius: 40px;
    width: 36px;
    height: 20px;
    border-radius: 4px;
    align-items: center;
    border: 0px solid #d8d2b3;
    // margin-left: -10px;
    color: #797B0B;
    font-size: 4px;
    background-color: rgba(225, 230, 96, 0.5);
    // background-color: #f2efc2;
}
</style>