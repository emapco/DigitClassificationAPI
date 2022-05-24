import{_ as C,d as P,r as d,q as T,a as r,c as I,e as t,u as o,w as a,s as u,v as p,x as _,m as h,B as f,y as m,z as b,b as e,t as s,A as v,j as l,p as R,i as x}from"./index.c2490d28.js";const n=i=>(R("data-v-01d32bba"),i=i(),x(),i),L={class:"accordian",role:"tablist"},D=l(" API endpoint: POST "),q=n(()=>e("code",null,"/api/file",-1)),A=n(()=>e("p",null,[l(" Send a request with a "),e("code",null,"<form>"),l(" marked with "),e("code",null,'enctype="multipart/form-data"'),l(". Within the form, include a "),e("code",null,"<input type=file name=image>"),l(" tag that contains the binary image file. The response is encoded in JSON. ")],-1)),U=n(()=>e("p",null,[e("u",null,"Python 3")],-1)),k=n(()=>e("p",null,[e("u",null,"JavaScript/TypeScript")],-1)),E=l(" API endpoint: POST "),J=n(()=>e("code",null,"/api/data",-1)),N=n(()=>e("p",null," Send a request with a base64 encoded image in the payload data. The response is encoded in JSON. ",-1)),O=n(()=>e("p",null,[e("u",null,"Python 3")],-1)),V=n(()=>e("p",null,[e("u",null,"JavaScript/TypeScript")],-1)),F=l(" Example API Response "),j=P({name:"ApiDocView",setup(i){const y=d(`
    import requests

    URL = 'http://127.0.0.1:5000/api/file'
    with open('img.png', 'rb') as file:
        files = {'image': file}
        response = requests.post(URL, files=files)
`),g=d(`
  URL = 'http://127.0.0.1:5000/api/file'
  async function uploadFile(form: HTMLFormElement) {
    const data = new FormData(form);
    const response = await fetch(FILE_URL, {
      method: "POST",
      mode: "cors",
      body: data
    });
    return response.json();
  }
`),S=d(`
    import base64
    import requests

    URL = 'http://127.0.0.1:5000/api/data'
    with open(img_path, 'rb') as file:
        b64_img_str = base64.b64encode(file.read())
        response = requests.post(url, data=b64_img_str)
`),w=d(`
  URL = 'http://127.0.0.1:5000/api/data'
  async function uploadImageData(b64EncodedImage: string) {
    const response = await fetch(URL, {
      method: "POST",
      mode: "cors",
      body: b64EncodedString
    });
    return response.json();
  }
`),B=d(`
  {
    "models": [
      {
        "name": "K Neighbors",
        "prediction": 3,
        "probabilities": {
          "0": 0.0,
          "1": 0.0,
          "2": 0.0,
          "3": 1.0,
          "4": 0.0,
          "5": 0.0,
          "6": 0.0,
          "7": 0.0,
          "8": 0.0,
          "9": 0.0
        }
      },
      {
        "name": "Random Forest",
        "prediction": 3,
        "probabilities": {
          "0": 0.03,
          "1": 0.06,
          "2": 0.11,
          "3": 0.35,
          "4": 0.07,
          "5": 0.18,
          "6": 0.02,
          "7": 0.04,
          "8": 0.07,
          "9": 0.06
        }
      }
    ]
  }`);return(H,z)=>{const c=T("b-toggle");return r(),I("div",L,[t(o(u),{"no-body":"",class:"mb-1"},{default:a(()=>[t(o(p),{"header-tag":"header",role:"tab"},{default:a(()=>[_((r(),h(o(f),null,{default:a(()=>[D,q]),_:1})),[[c,void 0,void 0,{"accordion-1":!0}]])]),_:1}),t(o(m),{id:"accordion-1",accordion:"my-accordion",role:"tabpanel"},{default:a(()=>[t(o(v),null,{default:a(()=>[t(o(b),null,{default:a(()=>[A,U,e("code",null,[e("pre",null,"            "+s(y.value)+`
          `,1)]),k,e("code",null,[e("pre",null,"            "+s(g.value)+`
          `,1)])]),_:1})]),_:1})]),_:1})]),_:1}),t(o(u),{"no-body":"",class:"mb-1"},{default:a(()=>[t(o(p),{"header-tag":"header",role:"tab"},{default:a(()=>[_((r(),h(o(f),{block:""},{default:a(()=>[E,J]),_:1})),[[c,void 0,void 0,{"accordion-2":!0}]])]),_:1}),t(o(m),{id:"accordion-2",accordion:"my-accordion",role:"tabpanel"},{default:a(()=>[t(o(v),null,{default:a(()=>[t(o(b),null,{default:a(()=>[N,O,e("code",null,[e("pre",null,"            "+s(S.value)+`
          `,1)]),V,e("code",null,[e("pre",null,"            "+s(w.value)+`
          `,1)])]),_:1})]),_:1})]),_:1})]),_:1}),t(o(u),{"no-body":"",class:"mb-1"},{default:a(()=>[t(o(p),{"header-tag":"header",role:"tab"},{default:a(()=>[_((r(),h(o(f),{block:""},{default:a(()=>[F]),_:1})),[[c,void 0,void 0,{"accordion-3":!0}]])]),_:1}),t(o(m),{id:"accordion-3",accordion:"my-accordion",role:"tabpanel"},{default:a(()=>[t(o(v),null,{default:a(()=>[t(o(b),null,{default:a(()=>[e("code",null,[e("pre",null,"            "+s(B.value)+`
          `,1)])]),_:1})]),_:1})]),_:1})]),_:1})])}}});var M=C(j,[["__scopeId","data-v-01d32bba"]]);export{M as default};
