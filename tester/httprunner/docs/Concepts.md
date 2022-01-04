### 前置准备工作-术语和概念

&nbsp;  
**测试步骤**  
测试步骤是最小的用例组织单元, 对应的是一个实际的测试动作.    
目前, 在`httprunner`框架中只支持`http/https`协议的`Step`, 后续需要扩展.  

> 测试步骤对齐编程语言中的函数

&nbsp;  
**测试用例**  
测试用例是测试步骤的集合.  
测试用例可以硬编测试步骤.  
测试用例可以引用已定义好的测试步骤.    
测试用例可以引用已定义好的子测试用例(模板).  
测试用例可以根据`HAR`文件生成(已支持), 对应的用例是多个硬编测试步骤的集合, 优点是写用例快, 缺点是接口发生变更时不易维护.    
测试用例可以根据`postman`用例生成(尚未支持), 对应的用例是多个硬编测试步骤的集合, 优点是写用例快, 缺点是接口发生变更时不易维护.    
测试用例可以根据`swagger`用例生成(尚未支持), 对应的用例是多个硬编测试步骤的集合, 优点是写用例快, 缺点是接口发生变更时不易维护.    


&nbsp;  
**会话变量**  
定义在测试步骤中的变量, 被称为会话变量(session_variables), 对应在编程中的术语是本地变量.  

> 会话变量对齐编程语言中的函数变量(function_variable)  
> 会话变量对齐pytest中的函数作用域([function scope](https://docs.pytest.org/en/6.2.x/fixture.html#fixture-scopes))  


&nbsp;  
**模块变量**  
定义在测试用例的公共部分的变量, 被称为模块变量(module_variables).  
模块变量有两种形式, 第一种是子用例中的模块变量; 第二种是父用例中的模板变量.  
默认情况下, 父用例无法访问子用例中的模块变量, 需要由子用例将模块变量export推送到上层, 父用例才能访问到子用例的模块变量.  

> 会话变量对齐编程语言中的模块变量(module variables / file variables)  
> 会话变量对齐pytest中的函数作用域([module scope](https://docs.pytest.org/en/6.2.x/fixture.html#fixture-scopes))  