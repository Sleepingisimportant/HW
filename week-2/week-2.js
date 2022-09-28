// 要求一:函式與流程控制
// 完成以下函式，在函式中使用迴圈計算最小值到最大值之間，固定間隔的整數總和。其中你可 以假設 max 一定大於 min 且為整數，step 為正整數。


//JavaScript
function calculate(min, max, step) {
    // 請用你的程式補完這個函式的區塊 
    let x = min;
    let total = min;
    while (x < max) {
        x += step;
        if (x > max) {
            break
        }
        total += x;
    }

    console.log(total)
}


calculate(1, 3, 1); // 你的程式要能夠計算 1+2+3，最後印出 6 
calculate(4, 8, 2); // 你的程式要能夠計算 4+6+8，最後印出 18 
calculate(-1, 2, 2); // 你的程式要能夠計算 -1+1，最後印出 0


// 要求二:Python 字典與列表、JavaScript 物件與陣列
// 完成以下函式，正確計算出非 manager 的員工平均薪資，所謂非 manager 就是在資料中 manager 欄位標註為 False (Python) 或 false (JavaScript) 的員工，程式需考慮員工資料數量 不定的情況。

function avg(data) {
    const d = data["employees"]
    let total = 0
    let num_non_manager = 0

    for (let i = 0; i < d.length; i++) {
        if (d[i]["manager"] === false) {
            total += d[i]["salary"]
            num_non_manager += 1
        }
    }

    let average = total / num_non_manager
    console.log(average)
}

avg({
    "employees": [{
        "name": "John", "salary": 30000, "manager": false
    }, {
        "name": "Bob", "salary": 60000, "manager": true
    }, {
        "name": "Jenny", "salary": 50000, "manager": false
    }, {
        "name": "Tony", "salary": 40000, "manager": false
    }]
});  // 呼叫 avg 函式



// 要求三:
// 完成以下函式，最後能印出程式中註解所描述的結果。



function func(a) {
    function multiply(b, c) {
        let result = a + (b * c)
        console.log(result)
        return result
    }
    return (multiply)

}
func(2)(3, 4); // 你補完的函式能印出 2+(3*4) 的結果 14 
func(5)(1, -5); // 你補完的函式能印出 5+(1*-5) 的結果 0 
func(-3)(2, 9); // 你補完的函式能印出 -3+(2*9) 的結果 15 
// 一般形式為 func(a)(b, c) 要印出 a+(b*c) 的結果


//要求四:
//找出至少包含兩筆整數的列表 (Python) 或陣列 (JavaScript) 中，兩兩數字相乘後的最大值。 提醒:請勿更動題目中任何已經寫好的程式，不可以使用排序相關的內建函式。

function maxProduct(nums) {
    let list_length = nums.length

    if (list_length == 2) {
        console.log(nums[0] * nums[1])
    }
    else {
        var n1 = nums
        var n2 = nums

        let m1 = Math.max(...n1)
        n1 = n1.filter(function (e) { return e !== m1 })
        m1 *= Math.max(...n1)

        let m2 = Math.min(...n2)
        n2 = n2.filter(function (e) { return e !== m2 })
        m2 *= Math.min(...n2)

        if (m1 >= m2) {
            console.log(m1)
        }
        else {
            console.log(m2)
        }

    }
}
maxProduct([5, 20, 2, 6]) // 得到 120 
maxProduct([10, -20, 0, 3]) // 得到 30 
maxProduct([10, -20, 0, -3]) // 得到 60 
maxProduct([-1, 2]) // 得到 -2 
maxProduct([-1, 0, 2]) // 得到 0 或 -0 
maxProduct([5, -1, -2, 0]) // 得到 2 
maxProduct([-5, -2]) // 得到 10


//要求五:
//Given an array of integers, show indices of the two numbers such that they add up to a specific target. You can assume that each input would have exactly one solution, and you can not use the same element twice.

function twoSum(nums, target) {

    let result = []

    for (let i = 0; i < nums.length; i++) {

        if (nums.includes(target - nums[i]) && target != nums[i] * 2) {
            result.push(i)
        }
    }

    return result
}

let result = twoSum([2, 11, 7, 15], 9);
console.log(result); // show [0, 2] because nums[0]+nums[2] is 9


//要求六 ( Optional ):
//給定只會包含 0 或 1 兩種數字的列表 (Python) 或陣列 (JavaScript)，計算連續出現 0 的最大長度。

function maxZeros(nums) {
    if (!nums.includes(0)) {
        console.log(0)
        return 0
    }

    else {
        const listLength = nums.length
        let position = 0

        let maxZeroCount = 0
        let count = 0
        for (let i = 0; i < nums.length; i++) {
            if (nums[i] == 0) {
                count += 1

                if (position == listLength - 1) {
                    if (maxZeroCount < count) {
                        maxZeroCount = count
                    }
                    console.log(maxZeroCount)
                    return maxZeroCount
                }

                else {
                    position += 1

                }
            }
            else {
                if (position == listLength - 1) {
                    if (maxZeroCount < count) {
                        maxZeroCount = count
                    }
                    console.log(maxZeroCount)
                    return maxZeroCount
                }

                else {
                    if (maxZeroCount < count) {
                        maxZeroCount = count
                    }
                    count = 0
                    position += 1
                }

            }

        }
    }
}
maxZeros([0, 1, 0, 0]); // 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]); // 得到 4 
maxZeros([1, 1, 1, 1, 1]); // 得到 0 
maxZeros([0, 0, 0, 1, 1]) // 得到 3