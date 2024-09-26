//제이쿼리 선언

// 전역변수
let num = 0;
let num2 = 0;

$(function(){

  // right 버튼 클릭
  $("#right").on("click", function(){
    //alert("우측버튼");
    if(num>=900){
      alert("오른쪽 끝에 도달했습니다. 우측 이동 불가.");
      return false;
    }
    $("#box").stop();
    num += 100;
    num2 += 360;

    $("#box").animate({
      left: num, "rotate" : num2+"deg"
    }, 500); // 우측버튼 애니메이트 1초동안
  }); // right 버튼 클릭

  // left 버튼 클릭
  $("#left").on("click", function(){
    //alert("좌측버튼");
    if(num<=0){
      alert("왼쪽 끝에 도달했습니다. 좌측 이동 불가.");
      return false;
    }
    
    $("#box").stop();
    num -= 100;
    num2 -= 360;
    $("#box").animate({
      left: num, "rotate" : num2+"deg"
    }, 500); // 좌측 애니메이트
  }); // left 버튼 클릭

}); //쿼리 끝
