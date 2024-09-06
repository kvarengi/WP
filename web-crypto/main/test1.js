window.onload = function(){
    let transactionKeys = [];
    for (let i = 0; i < localStorage.length; i++) {
      const key = localStorage.key(i);
      if (key.startsWith("put-transaction-") || key.startsWith("call-transaction-")) {
        const transactionValue = JSON.parse(localStorage.getItem(key));
        console.log(transactionValue)
        transactionKeys.push({ key: key, timestamp: transactionValue.timestamp, 
            year: transactionValue.year, month: transactionValue.month,
            day: transactionValue.day,
            date: transactionValue.time
         });
      }
    }
  
    console.log(transactionKeys)
    const transactionsArea = document.getElementById("transactions-area");
    if (transactionKeys.length > 0) {
      transactionKeys.sort((a, b) => {
        return a.timestamp - b.timestamp;
      }).forEach((item) => {
        const transactionValue = JSON.parse(localStorage.getItem(item.key));
        const spanElement = document.createElement("span");
        spanElement.className = "strans"
        const td = (transactionValue.day < 10 ? '0' : '') + transactionValue.day
        const tm = (transactionValue.month < 10 ? '0' : '') + transactionValue.month
        const tmins = (transactionValue.minutes < 10 ? '0' : '') + transactionValue.minutes
        spanElement.innerHTML = `
          ${transactionValue.value}<br>
          ${transactionValue.year}-${tm}-${td}  
          ${transactionValue.hours}:${tmins}

        `;
        transactionsArea.appendChild(spanElement);
      });
    } else {
        const newdiw = document.createElement("div", { class: "expanding-list" });
        newdiw.innerHTML = "<h1>Have no transactions.</h1>";
        newdiw.className = "ntrans"
        transactionsArea.appendChild(newdiw);
    }
  }