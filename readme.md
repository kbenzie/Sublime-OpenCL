# sublime-lang

Provided in the repository are the source file for an improved version of the Sublime Text C\+\+ package which contains snippets and reserved word completions. When installed correctly this package overrides the default C\+\+ package without removing it. This has only been tested with Sublime Text 3 beta which as available on Linux Mint 15 or for download from [sublimetext.com](http://sublimetext.com).

# Installation

Download [this package](https://bitbucket.org/infektor/sublime-lang/downloads/C++.sublime-package), alternatively you can compress the contents of the C++ directory into a zip archive. Note: Only the files within the directory should be included in the archive and that the archive must not contain the .zip file extension.

The archive should be be placed in the following paths dependent on your operating system:

linux   : `~/.config/sublime-text-3/Installed Packages/C++.sublime-package`

windows : `C:\Users\<user-name>\AppData\Roaming\Sublime Text 3\Installed Packages`

osx     : `todo`

# Usage

## C\+\+.sublime-package

This package is a modified clone of the default C\+\+ package provided with Sublime Text 3 which provides the syntax, symbol, indentation, code snippets, and completion settings for the C and C++ programming languages. The only elements which have been added or modified are the code snippets and completions, following you will find an exhaustive list of these features.

### Snippets

Snippets provide a helpful means of avoiding repetitively typing boilerplate code whilst also placing the cursor exactly where it needs to be to enable the user to quickly enter valid code. The title of each of the following sections relates exactly to the text required to show the completion menu whilst writing code, selecting the snippet can be achieved by pressing either the `tab` or `enter` keys. The the code will be immediately stamped out with the cursor moved to the first useful place to enter code, moving through the insertion points is done using `tab` for forwards and `shift + tab` for backwards. Below the insertion points will be denoted with a `$n` where `n` starts at `1` for the first insertion point, rising consecutively, the final position is has the value `0`. In the event `$n` appears multiple times the same text will be inserted at all points at once unless otherwise stated. If an insertion point contains placeholder text it will be denoted as `${n:placeholder}`. Certain snippets contain regular expressions or variables but for ease of reading those will not be contained in below.

#### Include Header

Tigger: `include`

```
#include ${1:"}$2${1:"}$0
```

#### Main Function

Tigger: `main`

```
int main(${1:int argc, char const *argv[]})
{
	${0:/* code */}
	return 0;
}
```

#### Define Macro

Tigger: `define`

```
#ifndef $1
#define ${1:macro} ${2:value}
#endif
```

#### If Statement

Tigger: `if`

```
if(${1:condition})
{
	${0:/* code */}
}
```

#### Else Condition

Tigger: `else`

```
else
{
	${0:/* code */}
}
```

#### Switch Statement

Tigger: `switch`

```
switch(${1:condition})
{
${0:/* cases */}
default: ${2:/* catch all */}
	break;
}
```

#### Switch Case Statement

Tigger: `case`

```
case ${1:value}:
	${2:/* code */}
	break;$0
```

#### Ternary Operator

Trigger: `?`

```
(${1:condition}) ? ${2:true} : ${3:false}
```

#### Class Definition

Tigger: `class`

```
class ${1:filename}
{
public:
	$1(${2:arguments});
	~$1();

	${3:/* data */}
};$0
```

#### Struct Definition

Tigger: `struct`

```
struct ${1:{filename}}
{
	${2:/* data */}
}$3;$0
```

#### Enum Definition

Tigger: `enum`

```
enum ${1:name}
{
	${2:/* values */}
};$0
```

#### Union Definition

Tigger: `union`

```
union ${1:name}
{
	${2:/* data */}
}$3;$0
```

#### For Loop

Tigger: `for`

```
for(${1:int} ${3:i} = 0; $3 < ${2:count}; ${4:++}$3)
{
	${0:/* code */}
}
```

#### While Loop

Tigger: `while`

```
while(${1:condition})
{
	${0:/* code */}
}
```

#### Do While Loop

Tigger: `do`

```
do
{
	${0:/* code */}
} while (${1:condition});
```

#### Range For Loop

Tigger: `forr`

```
for(auto ${1:element} : ${2:container})
{
	${0:/* code */}
}
```

#### Vector For Loop

Tigger: `forv`

```
for(std::vector<$1>::iterator ${3:i} = $2.begin(); $3 != $2.end(); ++$3)
{
	${0:/* code */}
}
```

#### Namespace

Tigger: `namespace`

```
namespace $1
{
	${0:/* code */}
}
```

#### Template Definition

Tigger: `template`

```
template<typename ${1:T}> $0
```

#### Static Cast

Tigger: `static_cast`

```
static_cast<${1:T}*>(${2:pointer})$0
```

#### Reinterpret Cast

Tigger: `reinterpret_cast`

```
reinterpret_cast<${1:T}*>(${2:pointer})$0
```

#### Const Cast

Tigger: `const_cast`

```
const_cast<${1:T}*>(${2:pointer})$0
```

#### Dynamic Cast

Tigger: `dynamic_cast`

```
dynamic_cast<${1:T}*>(${2:pointer})$0
```

#### Sizeof Operator

Tigger: `sizeof`

```
sizeof($1)$0
```

#### Static Assert

Tigger: `static_assert`

```
static_assert(${1:condition}, "${2:message}");$0
```

#### Constant Expression

Trigger: `constexpr`

```
constexpr ${1:void} ${2:func}($3)
{
	${0:/* code */}
}
```

#### Try Catch Block

Tigger: `try`

```
try
{
	${1:/* code */}
}
catch(${2:...})
{
	${3:/* code */}	
}$0
```

#### Catch Block

Tigger: `catch`

```
catch(${1:...})
{
	${2:/* code */}
}$0
```

#### Type Definition

Tigger: `typedef`

```
typedef ${1:type} ${2:definition};
```

#### Type Identifier

Tigger: `typeid`

```
typeid($1)$0
```

#### Print Function

Tigger: `printf`

The printf and related functions use the original packages clever regular expression allowing multiple `%` format entries in the format string at `$1` which will then enable additional insertion comma separated points at the penultimate insertion point.

```
printf("${1:%s}\\n", $2)$0
```

#### File Print Function

Tigger: `fprintf`

```
fprintf(${1:stderr}, "${2:%s}\\n", $3)$0
```

#### String Print Function

Tigger: `sprintf`

```
sprintf(${1:cstring}, "${2:%s}\\n", $3)$0
```

#### Read File Into Vector

Tigger: `readfile`

```
std::vector<char> v;
if (FILE *fp = fopen(${1:"filename"}, "r"))
{
	char buf[1024];
	while (size_t len = fread(buf, 1, sizeof(buf), fp))
		v.insert(v.end(), buf, buf + len);
	fclose(fp);
}
```

#### std::map

Tigger: `map`

```
std::map<${1:key}, ${2:value}> ${3:map};$0
```

#### std::vector

Tigger: `vector`

```
std::vector<${1:char}> v;$0
```

### Completions

Completions are much simpler than snippets, these are simply words which will appear in the completion menu in any C or C\+\+ source file. Primarily these are the languages reserved words, with the addition of the most commonly used integer types, minus those which include snippets.

From C

```
auto
char
const
continue
default
double
enum
extern
float
goto
int
long
register
return
short
signed
static
unsigned
void
volatile
```

Common integer types

```
wchar_t
char16_t
char32_t
size_t
int8_t
int16_t
int32_t
int64_t
int_max_t
int_ptr_t
uint8_t
uint16_t
uint32_t
uint64_t
uint_max_t
uint_ptr_t
NULL
```

From C\+\+

```
alignas
alignof
asm
bool
compl
constexpr
decltype
delete
explicit
export
false
friend
inline
mutable
new
noexcept
nullptr
operator
private
protected
public
this
thread_local
throw
true
typename
using
virtual
```

The textual logic operators were also not included as they are not commonly used, however they can be enabled if so desired.

# Further work

* Install script
* OpenCL C language support
* OpenCL API function completion
* Extend template snippet to support multiple type parameters and possibly variadic templates
* Requests for improvements are welcome
