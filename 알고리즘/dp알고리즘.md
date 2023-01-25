## 동적계획법 (dp) dynamic programming
- 뜻이 좀 이상하다.. 전혀 dynamic 하지않다. 교수님한분은 '기억하며 풀기'라고 정의

> 이미 구한 부분문제의 답을 캐쉬에 저장해서 또 구해야 할 때 바로 답을 내놓고 쓸데없는 계산을 하지 말자고 말한다.

[동적계획법 참고자료1](https://shoark7.github.io/programming/algorithm/3-ways-to-get-binomial-coefficients)
[동적계획법 참고자료2](https://namu.wiki/w/%EB%8F%99%EC%A0%81%20%EA%B3%84%ED%9A%8D%EB%B2%95)
[동적계획법 참고자료3](https://rh-tn.tistory.com/32)


- 파스칼의 삼각형을 이용하면 이해하기가 쉽다.

1. 메모이제이션 해둘 공간(list)를 미리 확보해둔다. 2차원배열
2. 파스칼 삼각형의 y열 0번째 인덱스 (ex : xy[1][0], xy[12][0])와 x==y 인 인덱스 (ex : xy[2][2], xy[5][5]) 는 1로 처리해둔다.
3. 이후 이항계수(combination) 정의를 이용하여 푼다.(그림으로 보는게 이해하기 쉬움) => 
```
static int[][] dp;
 
static int binomial(int n, int r) {
	if(r == 0 || n == r) 
		return 1;
	if(dp[n][r] == 0) 
		dp[n][r] = binomial(n - 1, r - 1) + binomial(n - 1, r);
	return dp[n][r];
}
 
static int binomial(int n, int r) {
	for(int i = 0; i<n; i++) {
			// 0 ~ i 또는 0 ~ k 까지 중 작은 것을 택함 불필요한 것을 구하지 않기 위해서 
			for(int j = 0; j<=Math.min(i, r); j++) {
				if(j == 0 || j == i) 
					dp[i][j] = 1;
				else
					dp[i][j] = dp[i-1][j-1] + dp[i-1][j];
			}
		}
		return dp[n][r];
	}
}​
```


- 피보나치 수열을 간단히 풀면서 dp의 이해를 도울수 있다.

> 아래는 피보나치 수열 C++로 풀어보기 예시 (간단히 1차원리스트로 메모이제이션하였다.)

```
int memo[100]{}; //메모이제이션 공간. 전역 변수이므로 0으로 초기화
int fibonacci(unsigned int n)
{
  if (n<=1) //0번째, 1번째 피보나치 수
    return n;
  if (memo[n]!=0) //메모가 있는지 확인(0으로 초기화되었으므로 0이 아니라면 메모가 쓰인 것임)
    return memo[n]; //메모 리턴
  memo[n]=fibonacci(n-1) + fibonacci(n-2); //작은 문제로 분할
  return memo[n];
}
```