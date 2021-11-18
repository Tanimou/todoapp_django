
valueList=document.getElementById("checks")
text1 ="<s>  {{t.text}} </s>"
text2 ="  {{t.text}} "
var listArray=[]
var checkboxes=document.querySelectorAll(".checkbox")
for (checbox of checkboxes){
    checbox.addEventListener("click",function()
    {
        if(this.checked==true)
         {  listArray.push(this.value)
          console.log(listArray)
       
         
        }
        else
        {   listArray=listArray.filter(e=>e!==this.value)
            console.log(listArray)
    //  const python_process = spawner("pyton", ["./main/python.py", JSON.stringify(listArray)])
   }
    }
 
    ) 
  
}
