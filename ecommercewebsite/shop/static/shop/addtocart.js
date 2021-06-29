if(localStorage.getItem('cart')===null){
    var cart = {}
}else{
    cart = JSON.parse(localStorage.getItem('cart'))
} 

const handleClick=(id)=>{
    if(cart[id]!=undefined){
        quantity = cart[id][0]+1
        cart[id][0] = quantity
        cart[id][2] += parseFloat(document.getElementById('price'+id).innerHTML) 
      
    }else{
        quantity =1 
        item_name =  document.getElementById('nm'+id).innerHTML
        item_price = parseFloat(document.getElementById("price"+id).innerHTML)
        cart[id] = [quantity,item_name,item_price]  
        
        console.log(cart[id]);    
    }
    localStorage.setItem('cart',JSON.stringify(cart))
    
    let cart_item_display = document.getElementById('cart-items')
    cart_item_display.innerHTML ="Cart " + Object.keys(cart).length
}
let buttons = document.querySelectorAll('.addToCart')
buttons.forEach((button)=>(
    button.addEventListener("click",()=>handleClick(button.id))
    
))
