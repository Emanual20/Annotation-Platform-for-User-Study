import service from "../utils/request.js";
import { rsaEncrypt } from "../utils/rsa.js";

export function UpdatePasswordPost(postParams){
    return service.request({
        method:'post',
        url:postParams.url,
        data:{
            username: postParams.username,
            npassword: postParams.npassword,
            key: postParams.key,
            secretKey: rsaEncrypt(new Date().getTime()+':'+'www.baidu.com'+':'+'otherinfos')
        }
    })
}

export function RegisterUserPost(postParams){
    return service.request({
        method:'post',
        url:postParams.url,
        data:{
            emailaddress: postParams.emailaddress,
            // username: postParams.username,
            password: postParams.password,
            invitation_code: postParams.invitation_code,
            attrs: postParams.attrs,
            key: postParams.key,
            secretKey: rsaEncrypt(new Date().getTime()+':'+'www.baidu.com'+':'+'otherinfos')
        }
    })
}

export function SubmitClicklogPost(postParams){
    return service.request({
        method:'post',
        url:postParams.url,
        data:{
            emailaddress: postParams.emailaddress,
            username: postParams.username,
            infos: postParams.infos,
            key: postParams.key,
            secretKey: rsaEncrypt(new Date().getTime()+':'+'www.baidu.com'+':'+'otherinfos')
        }
    })
}