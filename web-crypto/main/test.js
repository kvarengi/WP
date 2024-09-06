window.onload = function(){
    localStorage.clear()
    let clickCounta = 0;
    let clickCountb = 0;
    const date = new Date()
    const day = date.getDate()
    const month = date.getMonth()
    const year = date.getFullYear()
    const hour = date.getHours()
    const minutes = date.getMinutes()


    document.getElementById("call-btn").onclick = function() {
    clickCounta++;
    console.log(year)
    const transactionKey = `call-transaction-${clickCounta}`;
    const transactionValue = {
        timestamp: Date.now(),
        value: `CallTransaction ${clickCounta}`,
        day: day,
        year: year,
        month: month,
        minutes: minutes,
        hours: hour,
    };
    localStorage.setItem(transactionKey, JSON.stringify(transactionValue));
    console.log(localStorage)
    }

    document.getElementById("put-btn").onclick = function() {
    clickCountb++;
    const transactionKey = `put-transaction-${clickCountb}`;
    const transactionValue = {
        timestamp: Date.now(),
        value: `PutTransaction ${clickCountb}`,
        day: day,
        year: year,
        month: month,
        minutes: minutes,
        hours: hour,
    };
    localStorage.setItem(transactionKey, JSON.stringify(transactionValue));
    }
}