// 템플릿 문자열
const num1 = 1;
const num2 = 2;
const result1 = 3;
const string1 = `${num1} 더하기 ${num2} 는 ${result1}`;

console.log(string1)

// 객체 리터럴
var sayNode = function() {
    console.log('Node')
};
var es = 'ES';
const newObject = {
    sayJS() {
        console.log('JS');
    },
    sayNode,
    [es + 6] : 'Fantastic',
};
newObject.sayNode();
newObject.sayJS();
console.log(newObject.ES6);

// 화살표 함수
function add1(x, y) {
    return x + y;
}

const add2 = (x, y) => {
    return x + y;
};

const add3 = (x, y) => x + y;

const add4 = (x, y) => (x + y);

function not1(x){
    return !x;
}

const not2 = x => !x;

// this 바인드 방식
var relationship1 = {
    name : 'zero',
    friends : ['nero', 'hero', 'xero'],
    logFriends : function () {
        var that = this; // relationship1을 가리키는 this를 that에 저장
        this.friends.forEach(function (friend) {
            console.log(that.name, friend);
        });
    },
};
relationship1.logFriends();

const relationship2 = {
    name : 'zero',
    friends : ['nero', 'hero', 'xero'],
    logFriends() {
        this.friends.forEach(friend => {
            console.log(this.name, friend);
        });
    },
};
relationship2.logFriends();