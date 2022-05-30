var updateBtns = document.getElementsByClassName('update-cart')

for(i=0; i<updateBtns.length; i++){
    updateBtns[i].addEventListener('click',function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId:', productId, 'Action:', action)

       console.log('USER:',user)
       if(user === 'AnonymousUser'){
           console.log('Not logged in')
       } else{
           addtocartForm(productId, action)
       }
    })
}

function addtocartForm(productId, action){
    console.log('Add to cart form clicked')

    var addtocart = {
        'dedication':null,
        'quantity':null,
    }

    addtocart.dedication = dedicationForm.dedication.value
    addtocart.quantity = dedicationForm.quantity.value

    console.log('addtocart', addtocart)

    var url = "/addtocart/"
    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'dedicationForm':addtocart, 'productId': productId, 'action':action}),
    })
    .then((response) => response.json())
    .then((data) => {
          console. log('Success:',data);
          alert('Item added to Cart');

          window.location.href = "{% url 'index' %}"
          
    })

  }