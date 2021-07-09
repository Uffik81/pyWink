document.title = 'player WINK';
var listChannels = null;
// zabava-live
// http://sdp.svc.iptv.rt.ru:8080/CacheClient/ncdxml/ChannelPackage/list_channels?channelPackageId=11818722&locationId=100001&from=0&to=2147483647
// X-Requested-With, Content-Type, x-smartlabs-mac-address, Range
// X-Requested-With: XMLHttpRequest
// Content-Type: application/json, text/plain, */*
// x-smartlabs-mac-address: 00:1a:79:21:41:58
// 
// +++++ Wink +++++
// GET https://wink.rt.ru/tv/
// https://s26037.cdn.ngenix.net/sdp/sth/nclogo1526305986160.png
// https://s26037.cdn.ngenix.net/sdp/sth/imp_stv517571047.jpg
//window.__REVISION__ = "v2021.05.05.1515";
//window.__IMAGES_URL__ = "https://s26037.cdn.ngenix.net";
//window.__ALICE_ID__ = "7ab25b6a-30ae-4a5a-a67c-7996068e89ba";
//window.__REQUEST_ID__ = "491c7ed77f6b530e73d7e0a8b647e283";
//window.__OMNICHAT__ ="";
//window.__PUBLIC_KEY_CAPTCHA__ = '6Lfr_pkUAAAAAAotvpbJ1pUirS8vdXfmQczg4DYg';
// POST https://cnt-odcv-itv01.svc.iptv.rt.ru/api/v2/portal/session_tokens
// body: {"fingerprint":"mHJFymgafeiba0kVum6OJ"}
// GET wss://cnt-lbrc-itv01.svc.iptv.rt.ru/ws?session_id=3d608f30-b1cd-11eb-afe4-f063f976f300:1951416:2237006:2
// Sec-WebSocket-Accept: lDOq0ZD8RXhyG7z98D4sZKipGX8=  94 33 aa d1 90 fc 45 78 72 1b bc fd f0 3e 2c 64 a8 a9 19 7f
// 
// POST https://cnt-lbrc-itv02.svc.iptv.rt.ru/event_collector
// {"events":[
//    {"utc":1620678062412,
//     "uid":"mHJFymgafeiba0kVum6OJ",
//     "session_id":"3d608f30-b1cd-11eb-afe4-f063f976f300:1951416:2237006:2",
//     "san":"ct_nc_web_portal",
//     "auth_mode":"anonymous",
//     "is_test":0,
//     "profile_id":590473,
//     "session_type":"demo",
//     "sw_version":"v2021.05.05.1515",
//     "external_link":"/tv/580",
//     "category":"Жизненный цикл продукта",
//     "action":"Запуск приложения",
//     "label":"Запуск",
//     "device_type":"NCWEB",
//     "user_value":5},
//    {"utc":1620678062414,
//     "uid":"mHJFymgafeiba0kVum6OJ",
//     "session_id":"3d608f30-b1cd-11eb-afe4-f063f976f300:1951416:2237006:2",
//     "san":"ct_nc_web_portal",
//     "home_mrf":"ct",
//     "current_mrf":"sth",
//     "home_location":100001,
//     "home_sub_location":100001,
//     "cur_location":400008,
//     "cur_sub_location":400008,
//     "real_ip":"194.156.184.119",
//     "category":"Жизненный цикл продукта",
//     "action":"Геолокация устройства",
//     "user_value":2},
//    {"utc":1620678062944,
//     "uid":"mHJFymgafeiba0kVum6OJ",
//     "session_id":"3d608f30-b1cd-11eb-afe4-f063f976f300:1951416:2237006:2",
//     "san":"ct_nc_web_portal",
//     "category":"Интерфейс",
//     "action":"Показ страницы",
//     "user_value":1,
//     "label":"tvchannel",
//     "title":"Всё ТВ",
//     "path":"/tv/580"}
// ]}
// Request URL: https://rum.ngenix.net/result?data=%7B%22jobid%22:%22b41587f9-c041-befa-b0c5-51120695ab0b%22,%22tasksGroupKey%22:%22wink.rt.ru%22,%22results%22:%5B%7B%22id%22:2957,%22success%22:true,%22domainLookupDuration%22:0,%22connectDuration%22:0,%22requestDuration%22:22,%22responseDuration%22:28,%22fetchDuration%22:30%7D%5D,%22resolverIP%22:%22194.190.110.243%22%7D&jsonp=_63a0a1f3ede006e65f75d9dfb91804ba
// data: {"jobid":"b41587f9-c041-befa-b0c5-51120695ab0b","tasksGroupKey":"wink.rt.ru","results":[{"id":2957,"success":true,"domainLookupDuration":0,"connectDuration":0,"requestDuration":22,"responseDuration":28,"fetchDuration":30}],"resolverIP":"194.190.110.243"}
// jsonp: _63a0a1f3ede006e65f75d9dfb91804ba
//{"sent_at":"2021-05-10T20:35:06.796Z","sdk":{"name":"sentry.javascript.browser","version":"6.3.4"}}
//{"type":"session"}
//{"sid":"e7a35bb1f238465aaa0cbb95a2a9f297","init":true,"started":"2021-05-10T20:35:06.793Z","timestamp":"2021-05-10T20:35:06.794Z","status":"ok","errors":0,"duration":1,"attrs":{"release":"v2021.05.05.1515","environment":"production","ip_address":"194.156.184.119"}}
// https://cnt-odcv-itv01.svc.iptv.rt.ru/api/v2/portal/channels?limit=30&offset=0&with_epg=true&epg_limit=3
// session_id: 3d608f30-b1cd-11eb-afe4-f063f976f300:1951416:2237006:2
// x-wink-version: v2021.05.05.1515

var urlChannels = 'https://cnt-lbrc-itv01.svc.iptv.rt.ru/api/v2/portal/channels?limit=30&offset=0&with_epg=true&epg_limit=3';
var url_580_option = 'https://cnt-lbrc-itv01.svc.iptv.rt.ru/api/v2/portal/channels/nc/580';
var url_hls_580 = 'https://zabava-htlive.cdn.ngenix.net/hls/CH_IDXTRAHD/variant.m3u8';
//var url_hls_580 = 'https://s72169.cdn.ngenix.net/hls/CH_VSETVHD_HLS/variant.m3u8';
// модификация 
var url_hls_580 = 'https://s72169.cdn.ngenix.net/hls/CH_EUROSPORT4K_HLS/variant.m3u8';
// ----- Wink -----  
const url_auth_json = 'https://f58516f1-f901-5e0b-8ec0-c4183fd9decb.rum-reflector.ngenix.net/data.json?jsonp=_2e06787aa36fd17923fd591e06ee1e48'; 
//var url_580_ts = 'https://a3569456030-s72169.cdn.ngenix.net/hls/CH_VSETVHD_HLS/bw3000000/playlist.m3u8?sid=SRV01&useseq=t';
var url_580_ts = 'https://a3569457540-zabava-htlive.cdn.ngenix.net/hls/CH_IDXTRAHD/bw4000000/playlist.m3u8?utcstart=1621969200';
var wink_session_id = '3d608f30-b1cd-11eb-afe4-f063f976f300:1951416:2237006:2';
var videoplayer = document.createElement('video');
videoplayer.width = 1280;
ctrlPlayer = document.createElement('source');
ctrlPlayer.src = url_580_ts;
ctrlPlayer.type = 'application/x-mpegURL';
videoplayer.id = 'hls-player';
videoplayer.appendChild(ctrlPlayer);
videoplayer.class='video-js vjs-default-skin';
videoplayer.height = 720;
videoplayer.controls = true;
videoplayer.playsInline = true;
videoplayer.autoplay = true;
videoplayer.preload = 'auto';

videoplayer.src = url_hls_580; //'https://s26037.cdn.ngenix.net/imo/transform/profile=mediumbanner376x240/images/c1sl8g62t9cd2rs2ohjg.jpg';
//videoplayer.poster = 'https://wink.rt.ru/assets/83a9828228b5b113560d152cdf20bf3e.png'; 

//setDefaultsHeaders({"X-Wink-Version":window.__REVISION__||""})
const iframe    = document.getElementById('iframe');
const iframeWin = iframe.contentWindow || iframe;
const iframeDoc = iframe.contentDocument || iframeWin.document;
//iframe.setAttribute("src","https://wink.rt.ru");
let script = iframeDoc.createElement('SCRIPT');

script.append(` var wink_session_id = '';
    function sendWithoutOrigin(url) {
    var request = new XMLHttpRequest();

    request.open('GET', url);
    request.setRequestHeader('accept','application/json, text/plain, */*');
    request.setRequestHeader('x-wink-version','v2021.05.05.1515');
    request.setRequestHeader('session_id',wink_session_id);
    request.onreadystatechange = function() {
        if(request.readyState === XMLHttpRequest.DONE) {
            if(request.status === 200) {
                console.log('GET succeeded.');
            }
            else {
                console.log('GET failed.');
            }
        }
    }
    request.send();
}`);

iframeDoc.documentElement.appendChild(script);

function getChannels(){

}

function getSessionId(){
    let jsonLoader = new XMLHttpRequest();
    jsonLoader.open('POST','https://cnt-odcv-itv01.svc.iptv.rt.ru/api/v2/portal/session_tokens')
    jsonLoader.onreadystatechange = (obj, e) => {
        if (jsonLoader.readyState == 4 && jsonLoader.status == 200){
            console.log(jsonLoader.responseText);
            let ret = JSON.parse(jsonLoader.responseText);
            wink_session_id = ret.session_id;
        }
    }
    jsonLoader.send('{"fingerprint":"mHJFymgafeiba0kVum6OJ"}');
    return wink_session_id;
}

function getListCannels(e){
    wink_session_id = getSessionId();
    iframeWin.url = 'https://wink.rt.ru/';
    iframeWin.wink_session_id  = wink_session_id;
    iframeWin.sendWithoutOrigin(urlChannels);
    var xObj = new XMLHttpRequest();
    //xObj.overrideMimeType("application/json");
    //xObj.withCredentials = true;
    //xObj.overrideMimeType("application/json, text/plain, */*"); 
    //xObj.open('GET', urlChannels, true);   
    //xObj.setRequestHeader('accept','application/json, text/plain, */*'); 
    //xObj.setRequestHeader('x-wink-version','v2021.05.05.1515');

    //xObj.setRequestHeader('session_id',wink_session_id);
    // etag: "93e6b0445486b823d761e8e2a620e05f1b71e23c"
    xObj.onreadystatechange = (obj, e) => {
        
        if (xObj.readyState === 4 && xObj.status === 200) {
            // 2. call your callback function
            e(xObj.responseText);
        }
        if(xObj.status === 401){
            // POST https://sentry.iptv.rt.ru/api/5/envelope/?sentry_key=a532fbe84193426890b2ea72583494e7&sentry_version=7
            // body: {"sent_at":"2021-05-19T20:20:15.842Z","sdk":{"name":"sentry.javascript.browser","version":"6.3.4"}}
            //{"type":"session"}
            //{"sid":"1a6a85cc750e4690b64b0f0cc10cf8c5","init":true,"started":"2021-05-19T20:20:15.841Z","timestamp":"2021-05-19T20:20:15.841Z","status":"ok","errors":0,"duration":0,"attrs":{"release":"v2021.05.05.1515","environment":"production"}}
            
            // OPTIONS https://cnt-odcv-itv01.svc.iptv.rt.ru/api/v2/portal/session_tokens
            // POSt https://cnt-odcv-itv01.svc.iptv.rt.ru/api/v2/portal/session_tokens
            // body: {"fingerprint":"mHJFymgafeiba0kVum6OJ"}
            // result: {"session_id":"9fbb66dc-b8df-11eb-afe4-f063f976f300:1951416:2237006:2","session_state":"demo"}
            // DNT,X-Mx-ReqToken,Keep-Alive,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type,X-Wink-Version,session_id
            let url_option = 'https://cnt-odcv-itv01.svc.iptv.rt.ru/api/v2/portal/session_tokens';
            let xObj1 = new XMLHttpRequest();
            xObj1.open('OPTIONS', url_option, true);
            xObj1.onreadystatechange = (obj, e) => {
                if (xObj1.status === 204){
                    // Повторно получаем сессию ид
                    wink_session_id = getSessionId();
                }
                alert(wink_session_id);
                xObj.setRequestHeader('session_id',wink_session_id);
                alert(xObj1.responseText);

            };
            xObj1.send(null);
        }
    };
    
    //xObj.send(null);

}

function loadCallBack(resp){
    listChannels = JSON.parse(resp);
    
}

document.addEventListener("DOMContentLoaded", function(event) { 
    var divWinkPlayer = document.getElementById('wink-player');
    divWinkPlayer.appendChild(videoplayer);
    var videopl = videojs('hls-player');
    videopl.play();
    //videoplayer.play();
    getListCannels((e) => {
        listChannels = JSON.parse(e);
        let log_debugs = document.getElementById('log_debugs');
        log_debugs.innerHTML = listChannels;
    });
});

