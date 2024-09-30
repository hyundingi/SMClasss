// 제이쿼리 선언
$(function(){

  $("#searchBtn").on("click", function(){
    alert("검색버튼 클릭");
    let surl = "https://apis.data.go.kr/B551011/PhotoGalleryService1/gallerySearchList1?serviceKey=Y%2BduMd7L0jpQJx4Q09xs0zpRg0z3FvIYfWQVMCwtC%2BEY33tNGgPCV8ehJtjvLj4dCCOS6koa0w%2Fw6W7qksNz4w%3D%3D&numOfRows=10&pageNo=1&MobileOS=ET&MobileApp=AppTest&arrange=A&_type=json&keyword=";
    let searchWord = $("#search_txt").val();
    surl += searchWord;    
    $.ajax({
      url: surl,
      type: "get",
      data: "",
      dataType: "json",
      success:function(data){
        alert("성공");
        console.log(data);

        galdata = "";
        console.log(data.response.body.items.item[0].galContentId)
        for (var i=0;i<data.response.body.items.item.length;i++){

          galdata += `<tr>`
          galdata += `<td>${data.response.body.items.item[i].galContentId}</td>`
          galdata += `<td>${data.response.body.items.item[i].galTitle}</td>`
          galdata += `<td>${data.response.body.items.item[i].galPhotographer}</td>`
          galdata += `<td>${data.response.body.items.item[i].galCreatedtime}</td>`
          galdata += `<td><img src ='${data.response.body.items.item[i].galWebImageUrl}'></td>`
          galdata += `</tr>`
        }
        console.log(galdata);
        $("#tbody").html(galdata);
      },
      error:function(){
        alert("실패");
      }
    }); //ajax

  }); // 검색버튼 클릭

}); //제이쿼리