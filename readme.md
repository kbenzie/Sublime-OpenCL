# sublime-lang

Provided in the repository are the source files for an improved version of the Sublime Text C\+\+ package which contains snippets and completions for reserved words and function like language constructs as well as a small number of other functions. When installed this package overrides the default C\+\+ package without removing it, to uninstall simply remove this package. At this has only been tested with Sublime Text 3 beta which available Ubuntu packages and on Windows as download from [sublimetext.com](http://sublimetext.com).

# Installation

The python script 'install.py' is the easiest method of installing the package from source. Simply run the script and it will search for the correct directory to install the package. Note that Mac OSX support should be functional but has not been tested, if there are any issues contact the maintainer.

Alternatively you can download the package [here](https://bitbucket.org/infektor/sublime-lang/downloads/C++.sublime-package) and install it manually in the appropriate location for your platform as listed below. Note however that this package may not be the most recent version and it is recommended to install from source when possible.

* Windows: %APPDATA%\Sublime Text 3\Installed Packages
* OS X: ~/Library/Application Support/Sublime Text 3/Installed Packages
* Linux: ~/.config/sublime-text-3/Installed Packages

# Usage

## C\+\+.sublime-package

This package is a modified clone of the default C\+\+ package provided with Sublime Text 3 which provides the syntax, symbol, indentation, code snippets, and completion settings for the C and C++ programming languages. The only elements which have been added or modified are the code snippets and completions, following you will find an exhaustive list of these features.

### Snippets

Snippets provide a helpful means of avoiding repetitively typing boilerplate code whilst also placing the cursor exactly where it needs to be to enable the user to quickly enter valid code. The title of each of the following sections relates exactly to the text required to show the completion menu whilst writing code, selecting the snippet can be achieved by pressing either the `tab` or `enter` keys. The the code will be immediately stamped out with the cursor moved to the first useful place to enter code, moving through the insertion points is done using `tab` for forwards and `shift + tab` for backwards. Below the insertion points will be denoted with a `$n` where `n` starts at `1` for the first insertion point, rising consecutively, the final position is has the value `0`. In the event `$n` appears multiple times the same text will be inserted at all points at once unless otherwise stated. If an insertion point contains placeholder text it will be denoted as `${n:placeholder}`. Certain snippets contain regular expressions or variables but for ease of reading those will not be contained in below.

#### Include Header

Tigger: `include`

```
#include ${1:"}$2${1:"}
```

Insertion Points:

1. Pressing '<' will insert a '>' at the end of the header path
2. The header path

#### Main Function

Tigger: `main`

```
int main(${1:int argc, char const *argv[]})
{
	${0:/* code */}
	return 0;
}
```

Insertion Points:

1. Edit or remove parameters

#### Define Macro

Tigger: `define`

```
#ifndef $1
#define ${1:macro} ${2:value}
#endif
```

Insertion Points:

1. Name of preprocessor marco
2. Optional value of macro

#### If Statement

Tigger: `if`

```
if(${1:condition})
{
	${0:/* code */}
}
```

Insertion Points:

1. Boolean condition

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

Insertion Points:

1. Variable to switch on
2. Default case code

#### Switch Case Statement

Tigger: `case`

```
case ${1:value}:
	${2:/* code */}
	break;
```

Insertion Points:

1. Case value
2. Insert code

#### Ternary Operator

Trigger: `?`

```
(${1:condition}) ? ${2:true} : ${3:false}
```

Insertion Points:

1. Boolean condition
2. True case
3. False case

#### Class Definition

Tigger: `class`

```
class ${1:filename}
{
public:
	$1(${2:arguments});
	~$1();

	${3:/* data */}
};
```

Insertion Points:

1. Inserts filename by default, constructor and destructor named automatically
2. Constructor arguments
3. Data members

#### Struct Definition

Tigger: `struct`

```
struct ${1:{filename}}
{
	${2:/* data */}
}$3;
```

Insertion Points:

1. Inserts filename by default
2. Data members
3. Optional: Insert instance name

#### Enum Definition

Tigger: `enum`

```
enum ${1:name}
{
	${2:/* values */}
};
```

Insertion Points:

1. Optional: Enum name
2. Enem values


#### Union Definition

Tigger: `union`

```
union ${1:name}
{
	${2:/* data */}
}$3;
```

Insertion Points:

1. Optional: Union name
2. Union data members
3. Optional: Instance name

#### For Loop

Tigger: `for`

```
for(${1:int} ${3:i} = 0; $3 < ${2:count}; ${4:++}$3)
{
	${0:/* code */}
}
```

Insertion Points:

1. Increment variable type
2. Loop end condition
3. Increment variable name
4. Increment operator

#### While Loop

Tigger: `while`

```
while(${1:condition})
{
	${0:/* code */}
}
```

Insertion Points:

1. Boolean condition

#### Do While Loop

Tigger: `do`

```
do
{
	${0:/* code */}
} while (${1:condition});
```

Insertion Points:

1. Boolean condition

#### Range For Loop

Tigger: `forr`

```
for(auto ${1:element} : ${2:container})
{
	${0:/* code */}
}
```

Insertion Points:

1. Iterator variable name
2. Container name

#### Vector For Loop

Tigger: `forv`

```
for(std::vector<$1>::iterator ${3:i} = $2.begin(); $3 != $2.end(); ++$3)
{
	${0:/* code */}
}
```

Insertion Points:

1. Vector element type
2. Vector name
3. Iterator variable name

#### Namespace

Tigger: `namespace`

```
namespace $1
{
	${0:/* code */}
}
```

Insertion Points:

1. Namespace name

#### Template Definition

Tigger: `template`

```
template<typename ${1:T}> $0
```

Insertion Points:

1. Tempalte type name

#### Static Cast

Tigger: `static_cast`

```
static_cast<${1:T}*>(${2:pointer})
```

Insertion Points:

1. Return type
2. Variable to cast

#### Reinterpret Cast

Tigger: `reinterpret_cast`

```
reinterpret_cast<${1:T}*>(${2:pointer})
```

Insertion Points:

1. Return type
2. Variable to cast

#### Const Cast

Tigger: `const_cast`

```
const_cast<${1:T}*>(${2:pointer})
```

Insertion Points:

1. Return type
2. Variable to cast

#### Dynamic Cast

Tigger: `dynamic_cast`

```
dynamic_cast<${1:T}*>(${2:pointer})
```

Insertion Points:

1. Return type
2. Variable to cast

#### Sizeof Operator

Tigger: `sizeof`

```
sizeof($1)
```

Insertion Points:

1. Variable or type

#### Lambda Function

Trigger: `[]`

```
[${1:capture}](${2:params}) $3{${4:
	}${5:/* code */}
$4}
```

Insertion Points:

1. Lambda capture
2. Function parameters
3. Optional: Return type
4. Optional: Press space to change to single line syntax
5. Insert code

#### Static Assert

Tigger: `static_assert`

```
static_assert(${1:condition}, "${2:message}");
```

Insertion Points:

1. Compile time constant
2. Assertion message

#### Constant Expression

Trigger: `constexpr`

```
constexpr ${1:void} ${2:func}($3)
{
	${0:/* code */}
}
```

Insertion Points:

1. Function return type
2. Function name
3. Function parameters

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
}
```

Insertion Points:

1. Insert code
2. Exception type
3. Insert code

#### Catch Block

Tigger: `catch`

```
catch(${1:...})
{
	${2:/* code */}
}
```

Insertion Points:

1. Exception type
2. Insert code

#### Type Definition

Tigger: `typedef`

```
typedef ${1:type} ${2:definition};
```

Insertion Points:

1. Existing type name
2. Defined type name

#### Type Identifier

Tigger: `typeid`

```
typeid($1)
```

Insertion Points:

1. Type name

#### Print Function

Tigger: `printf`

The printf and related functions use the original packages clever regular expression allowing multiple `%` format entries in the format string at `$1` which will then enable additional insertion comma separated points at the penultimate insertion point.

```
printf("${1:%s}\\n", $2)
```

Insertion Points:

1. Format string
2. Optional: Variables to print

#### File Print Function

Tigger: `fprintf`

```
fprintf(${1:stderr}, "${2:%s}\\n", $3)
```

Insertion Points:

1. Format string
2. Optional: Variables to print

#### String Print Function

Tigger: `sprintf`

```
sprintf(${1:cstring}, "${2:%s}\\n", $3)
```

Insertion Points:

1. Format string
2. Optional: Variables to print

#### Read File Into Vector

Tigger: `readfile`

```
std::vector<char> ${1:v};
if (FILE${TM_C_POINTER: *}fp = fopen(${2:"filename"}, "r"))
{
	char buf[1024];
	while (size_t len = fread(buf, 1, sizeof(buf), fp))
		v.insert(v.end(), buf, buf + len);
	fclose(fp);
}
```

Insertion Points:

1. Name of file to be read

#### std::map

Tigger: `map`

```
std::map<${1:key}, ${2:value}> ${3:map};
```

Insertion Points:

1. Map key type
2. Map value type
3. Map variable name

#### std::vector

Tigger: `vector`

```
std::vector<${1:char}> v;
```

Insertion Points:

1. Vector element type

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
