// 1. ajax를 사용하여 데이터 가져오기

// 전역변수
var count = 0;
var id_num;
var temp = 0;

//제이쿼리 선언
$(function(){

  $("#dataBtn").on("click", function(){

    //ajax 선언
    $.ajax({
      url: "js/stuData.json",
      type: "get",
      data: "",
      dataType: "",
    success:function(data){
      alert("데이터를 가져옵니다.");
      //console.log(data[0].math);

      var stuData = "";
      for (var i=0;i<data.length;i++){
        count++;
        var total = data[i].kor*1 + data[i].eng*1 + data[i].math*1
        var avg = (total/3).toFixed(2)
        stuData += `<tr id='${i}'>`
        stuData += `<td>${data[i].no}</td>`
        stuData += `<td>${data[i].name}</td>`
        stuData += `<td>${data[i].kor}</td>`
        stuData += `<td>${data[i].eng}</td>`
        stuData += `<td>${data[i].math}</td>`
        stuData += `<td>${total}</td>`
        stuData += `<td>${avg}</td>`
        stuData += `<td><button class='updateBtn'>수정</button><button class='delBtn'>삭제</button></td>`
        stuData += `</tr>`

      }
      $("#tbody").html(stuData);
    },
    error:function(){
      alert("실패");
    }
  }); // ajax 끝
}); // 데이터가져오기 버튼 클릭

  $("#create").on("click", function(){
    count++

    var inputData = "";
    var inputname = $("#name").val();
    var inputkor = $("#kor").val();
    var inputeng = $("#eng").val();
    var inputmath = $("#math").val();
    var inputtotal = $("#kor").val()*1 + $("#eng").val()*1 + $("#math").val()*1;
    var inputavg = (inputtotal/3).toFixed(2);

    
    if(inputname ==="" || inputkor ==="" || inputeng ==="" || inputmath ===""){
      alert("빈칸없이 입력하세요");
      return false;
    }

    inputData += `<tr id='${count}'>`
    inputData += `<td>${count}</td>`
    inputData += `<td>${inputname}</td>`
    inputData += `<td>${inputkor}</td>`
    inputData += `<td>${inputeng}</td>`
    inputData += `<td>${inputmath}</td>`
    inputData += `<td>${inputtotal}</td>`
    inputData += `<td>${inputavg}</td>`
    inputData += `<td><button class='updateBtn'>수정</button><button class='delBtn'>삭제</button></td>`
    inputData += `</tr>`
    
    $("#tbody").prepend(inputData);
    alert("입력이 완료되었습니다.");

    $("#name").val("");
    $("#kor").val("");
    $("#eng").val("");
    $("#math").val("");
    

  }); // 입력 버튼 클릭

  $(document).on("click", ".delBtn", function(){
    console.log($(this).parent().parent().attr("id"));

    var id_num = $(this).parent().parent().attr("id");
    if(confirm("삭제하시겠습니까?")){
      $("#"+id_num).remove();
      alert("삭제되었습니다.")
    }
  }); // 삭제버튼 클릭

  $(document).on("click", ".updateBtn", function(){
    var id_num = $(this).parent().parent().attr("id");
    var redata = $("#"+id_num).children();

    alert("수정을 진행합니다.");
    temp++;
    if(temp > 1){
      alert("현재 수정을 완료하세요.");
      return false;
    }
    //표 데이터 가져오기
    //console.log(redata.text());
    $("#name").val(redata[1].textContent) // 이름
    $("#kor").val(redata[2].textContent) // 국어
    $("#eng").val(redata[3].textContent) // 영어
    $("#math").val(redata[4].textContent) // 수학
    $("#create, #update, #updateCancel").toggle();



    $(document).on("click", "#update", function(){

      temp = 0;
      //입력된 데이터 가져오기
      var rename = $("#name").val();
      var rekor = $("#kor").val()*1;
      var reeng = $("#eng").val()*1;
      var remath = $("#math").val()*1;
      var retotal = rekor+reeng+remath;
      var reavg = (retotal/3).toFixed(2);
      var inputData = "";
      // 수정 입력된 데이터 표에 넣기
      inputData += `<td>${id_num}</td>`
      inputData += `<td>${rename}</td>`
      inputData += `<td>${rekor}</td>`
      inputData += `<td>${reeng}</td>`
      inputData += `<td>${remath}</td>`
      inputData += `<td>${retotal}</td>`
      inputData += `<td>${reavg}</td>`
      inputData += `<td><button class='updateBtn'>수정</button><button class='delBtn'>삭제</button></td>`


      $("#"+id_num).html(inputData);
      
      alert("수정이 완료되었습니다.");
      $("#create, #update, #updateCancel").toggle();
     

      $("#name").val("");
      $("#kor").val("");
      $("#eng").val("");
      $("#math").val("");


    }); //  수정버튼

    $("#")

  }); //수정 버튼 클릭

  $("#updateCancel").on("click", function(){
    alert("수정이 취소됩니다.");
    $("#create, #update, #updateCancel").toggle();
    $("#name").val("");
    $("#kor").val("");
    $("#eng").val("");
    $("#math").val("");
    temp = 0;
  })




}); // 제이쿼리 끝