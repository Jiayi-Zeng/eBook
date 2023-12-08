"use strict";(self.webpackChunk=self.webpackChunk||[]).push([[349],{47228:function(A,g,t){t.d(g,{Z:function(){return x}});var u=t(42122),c=t.n(u),p=t(94184),d=t.n(p),n=t(15867),m=t(86074),f=function(a){return(0,m.jsx)(n.ZP,c()(c()({},a),{},{className:d()("normal-btn",a.className),type:"primary"}))},x=f},12168:function(A,g,t){t.d(g,{Z:function(){return x}});var u=t(42122),c=t.n(u),p=t(94184),d=t.n(p),n=t(58724),m=t(86074),f=function(a){return(0,m.jsx)(n.Z,c()(c()({},a),{},{className:d()("normal-input",a.className)}))},x=f},42628:function(A,g,t){t.d(g,{Z:function(){return B}});var u=t(42122),c=t.n(u),p=t(27424),d=t.n(p),n=t(86074),m=function(v){return(0,n.jsx)("div",{className:"question-item-base",children:v.children})},f=t(2453),x=t(78045),e=t(78957),a=t(62435),o=function(v){var h,M=f.ZP.useMessage(),j=d()(M,2),T=j[0],N=j[1],P=v,S=(0,a.useState)(-1),C=d()(S,2),H=C[0],L=C[1],O=function(){T.open({type:"success",content:"\u56DE\u7B54\u6B63\u786E"})},$=function(){T.open({type:"error",content:"\u56DE\u7B54\u9519\u8BEF"})},U=function(y){L(y.target.value),y.target.value==P.answer?O():$()};return(0,n.jsxs)(m,{children:[N,(0,n.jsx)("div",{className:"question-item-title",children:P.title}),(0,n.jsx)("div",{className:"question-item-question",dangerouslySetInnerHTML:{__html:P.question}}),(0,n.jsx)(x.ZP.Group,{className:"question-item-options",onChange:U,value:H,children:(0,n.jsx)(e.Z,{direction:"vertical",children:(h=P.options)===null||h===void 0?void 0:h.map(function(Z,y){return(0,n.jsx)(x.ZP,{value:Z.id,children:Z.choice_text},String(y))})})})]})},r=o,s=t(47228),l=t(12168),I=function(v){var h=f.ZP.useMessage(),M=d()(h,2),j=M[0],T=M[1],N=v,P=(0,a.useState)(),S=d()(P,2),C=S[0],H=S[1],L=function(y){H(y.target.value)},O=function(y){C==N.answer?$():U()},$=function(){j.open({type:"success",content:"\u56DE\u7B54\u6B63\u786E"})},U=function(){j.open({type:"error",content:"\u56DE\u7B54\u9519\u8BEF"})};return(0,n.jsxs)(m,{children:[T,(0,n.jsx)("div",{className:"question-item-title",children:N.title}),(0,n.jsx)("div",{className:"question-item-question",dangerouslySetInnerHTML:{__html:N.question}}),(0,n.jsxs)("div",{className:"question-item-input",children:[(0,n.jsx)(l.Z,{placeholder:"\u8F93\u5165\u7B54\u6848",value:C,onChange:L}),(0,n.jsx)(s.Z,{onClick:O,children:"\u63D0\u4EA4"})]})]})},i=I,E=function(v){switch(v.type){case"completion":return(0,n.jsx)(i,c()({},v.info));case"choice":return(0,n.jsx)(r,c()({},v.info))}},B=E},63872:function(A,g,t){t.r(g),t.d(g,{default:function(){return o}});var u=t(27424),c=t.n(u),p=t(93578),d=t(42628),n=t(62435),m=t(26330),f=function(){return(0,m.ZP)("get","/api/question/",null)},x=function(){return(0,m.ZP)("get","/api/choice/",null)},e=t(86074),a=function(){var s=(0,p.UO)(),l=Number(s.id),I=(0,n.useState)(),i=c()(I,2),E=i[0],B=i[1];return(0,n.useEffect)(function(){f().then(function(Q){var v=Q;v.forEach(function(h,M){if(h.id==l){var j={id:h.id,title:h.question_text,question:h.body,answer:h.correct_choice_id,options:[]};return x().then(function(T){var N=T,P=[];N.forEach(function(S,C){S.question_id==j.id&&P.push(S)}),j.options=P.sort(function(S,C){return S.sort_order-C.sort_order}),B(j)}),!1}})})},[]),(0,n.useEffect)(function(){parent.postMessage({type:"resize"},"*")},[E]),(0,e.jsx)("div",{children:(0,e.jsx)(d.Z,{type:"choice",info:E})})},o=a},26330:function(A,g,t){t.d(g,{ZP:function(){return m}});var u=t(6154);u.Z.defaults.timeout=1e5,u.Z.defaults.baseURL="http://47.103.202.117/",u.Z.interceptors.request.use(function(e){return e.data=String(e.data),e.headers["Content-Type"]="application/json",e},function(e){return Promise.reject(e)}),u.Z.interceptors.response.use(function(e){return e},function(e){console.log("\u8BF7\u6C42\u51FA\u9519\uFF1A",e)});function c(e){var a=arguments.length>1&&arguments[1]!==void 0?arguments[1]:{};return new Promise(function(o,r){u.Z.get(e,{params:a}).then(function(s){s?o(s.data):r(s)}).catch(function(s){r(s)})})}function p(e,a,o){return new Promise(function(r,s){u.Z.post(e,a,{headers:o}).then(function(l){l?r(l.data):s(l)}).catch(function(l){s(l)})})}function d(e){var a=arguments.length>1&&arguments[1]!==void 0?arguments[1]:{};return new Promise(function(o,r){axios.patch(e,a).then(function(s){o(s.data)},function(s){f(s),r(s)})})}function n(e){var a=arguments.length>1&&arguments[1]!==void 0?arguments[1]:{};return new Promise(function(o,r){axios.put(e,a).then(function(s){o(s.data)},function(s){f(s),r(s)})})}function m(e,a,o){var r=arguments.length>3&&arguments[3]!==void 0?arguments[3]:void 0,s="";return new Promise(function(l,I){switch(e){case"get":console.log("begin a get request,and url:",a),c(a,o).then(function(i){l(i)}).catch(function(i){console.log("get request GET failed.",i),I(i)});break;case"post":p(a,o,r).then(function(i){l(i)}).catch(function(i){console.log("get request POST failed.",i),I(i)});break;default:break}})}function f(e){if(e&&e.response)switch(e.response.status){case 400:alert(e.response.data.error.details);break;case 401:alert("\u672A\u6388\u6743\uFF0C\u8BF7\u767B\u5F55");break;case 403:alert("\u62D2\u7EDD\u8BBF\u95EE");break;case 404:alert("\u8BF7\u6C42\u5730\u5740\u51FA\u9519");break;case 408:alert("\u8BF7\u6C42\u8D85\u65F6");break;case 500:alert("\u670D\u52A1\u5668\u5185\u90E8\u9519\u8BEF");break;case 501:alert("\u670D\u52A1\u672A\u5B9E\u73B0");break;case 502:alert("\u7F51\u5173\u9519\u8BEF");break;case 503:alert("\u670D\u52A1\u4E0D\u53EF\u7528");break;case 504:alert("\u7F51\u5173\u8D85\u65F6");break;case 505:alert("HTTP\u7248\u672C\u4E0D\u53D7\u652F\u6301");break;default:}}function x(e,a,o){o.code}}}]);