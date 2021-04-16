var smartPixelConfig={fixed:[3000129,null],timeOnSite:[[5,2000167,null]],
    dmpDomain:"rtb-eu.b.otm-r.com/spevent"};!function(e,s){"use strict"
    ;var t=function(e){if(!(this instanceof t))return new t(e);this.data=e,
    this._qseg={},this._rseg={},this._uhtml={},setTimeout(this._checker.bind(this),
    10)},n=t;function a(){this.onload=this.onerror=null}n.fn=n.prototype,
    n.fn._checker=function(){var t=this,e=Object.keys(t._qseg).filter(function(e){
    return!t._rseg[e]});for(var n in t._qseg={},e)t._rseg[e[n]]=!0;if(0<e.length){
    var a="https://"+t.data.dmpDomain+"?sadd="+encodeURIComponent(e.join(",")
    )+"&r="+Math.random();t._addPix(a)}setTimeout(t._checker.bind(t),500)},
    n.fn._addPix=function(e){if(!this.data.cDomainName||~location.hostname.indexOf(
    this.data.cDomainName)){var t=new Image(1,1);t.onload=t.onerror=a,t.src=e}},
    n.fn.addSeg=function(e){e&&"0"!=e&&(this._qseg[e]=!0)},n.fn.addSegRx=function(e,
    t,n,a,i,r){this.addSegCond(e,{rx:t,mod:n},"rx",a,i,r)},
    n.fn.addUserHtml=function(e,t){if(!(
    "string"!=typeof e||""===e||void 0!==t&&this._uhtml[t])){this._uhtml[t]=!0,
    e=e.replace(/document\.write(?:ln)?/g,"mSmartPixel.addUserHtml")
    ;var n=s.createElement("span");n.innerHTML=e;var a=n.getElementsByTagName(
    "script");for(var i in a)if(a.hasOwnProperty(i)){var r=s.createElement("script")
    ;a[i].text&&(r.text=a[i].text),a[i].src&&(r.src=a[i].src),a[i].type&&(
    r.type=a[i].type),s.head.appendChild(r).parentNode.removeChild(r)}
    s.head.appendChild(n)}},n.fn.addSegCond=function(e,t,n,a,i,r){var s=!1;switch(
    -1<["<","<=",">",">="].indexOf(n)&&(e=Number(e),t=Number(t)),n){case"rx":
    s=new RegExp(t.rx,t.mod).test(e);break;case"<":s=e<t;break;case"<=":s=e<=t;break
    ;case"==":s=e==t;break;case">":s=t<e;break;case">=":s=t<=e;break;case"!=":s=e!=t
    ;break;case"inc":s=e&&-1<e.indexOf(t);break;case"!inc":s=-1===(e||[]).indexOf(t)
    ;break;case"i":s=new RegExp(t,"i").test(e)}return s&&(this.addSeg(a),
    this.addUserHtml(i,r)),!!s},window.mSmartPixel=n(e)}(smartPixelConfig,document),
    function(e){"use strict";var t=e.data.fixed;e.addSeg(t[0]),e.addUserHtml(t[1],
    "fixed")}(mSmartPixel),function(o){"use strict";var e="_spLd";!function e(t,n,a
    ){for(var i=Date.now()-a.ltime,r=0;r<n.length;r++){var s=n[r]
    ;a.flags[r]||i/1e3>s[0]&&(o.addSeg(s[1]),o.addUserHtml(s[2],"timeOnSite_"+r),
    a.flags[r]=!0)}!function(e,t){var n,a,i=e.ltime.toString();for(var r in e.flags
    )i+="!"+r;n=t,a=i,document.cookie=n+"="+encodeURIComponent(a)}(a,t),setTimeout(e
    ,1e3,t,n,a)}(e,o.data.timeOnSite,function(e){var t={ltime:Date.now(),flags:{}},
    n=(a=e,i=new RegExp("(?:(?:^|.*;\\s*)"+a+"\\s*\\=\\s*([^;]*).*$)|^.*$"),
    decodeURIComponent(document.cookie.replace(i,"$1"))).split("!").filter(function(
    e){return e});var a,i;0<n.length&&(t.ltime=Math.floor(n.shift()));for(
    var r=0;r<n.length;r++)t.flags[n[r]]=!0;return t}(e))}(mSmartPixel);
    