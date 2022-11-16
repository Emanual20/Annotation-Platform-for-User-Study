import service from "../utils/request.js";
import { rsaEncrypt } from "../utils/rsa.js";

export function GetInfo(){
    return service.request({
        method: "get",
        url: "/user_stuinfos"
    })
};

export function GetStudents(){
    return service.request({
        method: "get",
        url: "/get_stuinfos"
    })
}

export function GetInfoPost(postParams){
    return service.request({
        method:'post',
        url: postParams.url,
        data:{
            key: postParams.key,
            secretKey: rsaEncrypt(new Date().getTime()+':'+'www.baidu.com'+':'+'otherinfos')
        }
    })
}

export function CheckPwPost(postParams){
    return service.request({
        method:'post',
        url:postParams.url,
        data:{
            username: postParams.username,
            password: postParams.password,
            key: postParams.key,
            secretKey: rsaEncrypt(new Date().getTime()+':'+'www.baidu.com'+':'+'otherinfos')
        }
    })
}

export function FetchDisplayinfoPost(postParams){
    return service.request({
        method:'post',
        url:postParams.url,
        data:{
            username: postParams.username,
            displaynum: postParams.displaynum,
            key: postParams.key,
            secretKey: rsaEncrypt(new Date().getTime()+':'+'www.baidu.com'+':'+'otherinfos')
        }
    })
}

export function FetchDisplayCombinationinfoPost(postParams){
    return service.request({
        method:'post',
        url:postParams.url,
        data:{
            username: postParams.username,
            displaynum: postParams.displaynum,
            key: postParams.key,
            secretKey: rsaEncrypt(new Date().getTime()+':'+'www.baidu.com'+':'+'otherinfos')
        }
    })
}

export function FetchDisplayNewPost(postParams){
    return service.request({
        method:'post',
        url:postParams.url,
        data:{
            username: postParams.username,
            displaynum: postParams.displaynum,
            key: postParams.key,
            secretKey: rsaEncrypt(new Date().getTime()+':'+'www.baidu.com'+':'+'otherinfos')
        }
    })    
}