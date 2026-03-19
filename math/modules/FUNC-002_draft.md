```yaml
MODULE_ID: HS-FUNC-002
TITLE: "Quadratic Functions"
LEVEL: 高校数学（国際標準）
OBJECTIVE: "Quadratic functions' properties are understood, graphs are drawn, max-min problems are solved, and equations are solved."
CORE_CONCEPTS:
- "Parabola": A U-shaped graph representing quadratic functions. Key features include vertex, axis of symmetry, and direction of opening.
- "Vertex Form": $ y = a(x-h)^2 + k $, where $ (h,k) $ is the vertex. The coefficient $ a $ determines direction and width.
- "Discriminant": $ \Delta = b^2 - 4ac $, determines the number of real roots: $ \Delta > 0 $ (two real roots), $ \Delta = 0 $ (one real root), $ \Delta < 0 $ (no real roots).
- "Max-Min Problems": Optimization problems using vertex form or completing the square to find maximum/minimum values.
- "Axis of Symmetry": $ x = \frac{-b}{2a} $, vertical line dividing the parabola into two mirror images.

---

### Introduction  
Quadratic functions are defined as $ f(x) = ax^2 + bx + c $, where $ a \neq 0 $. Their graphs are parabolas, symmetric about the axis of symmetry $ x = \frac{-b}{2a} $. Key properties include:  
- **Vertex**: The highest or lowest point of the parabola, located at $ \left( \frac{-b}{2a}, f\left( \frac{-b}{2a} \right) \right) $.  
- **Direction of Opening**: If $ a > 0 $, the parabola opens upwards; if $ a < 0 $, it opens downwards.  
- **Roots**: Solutions to $ ax^2 + bx + c = 0 $, determined by the discriminant $ \Delta = b^2 - 4ac $.  

---

### Core Concepts  

#### 1. Parabola  
A parabola is a U-shaped curve. Its graph is determined by the quadratic function $ f(x) = ax^2 + bx + c $.  
- **Vertex**: The point $ (h, k) $ where $ h = \frac{-b}{2a} $, $ k = f(h) $.  
- **Axis of Symmetry**: The vertical line $ x = h $.  
- **Direction of Opening**: $ a > 0 $ → up; $ a < 0 $ → down.  

#### 2. Vertex Form  
The vertex form of a quadratic function is $ y = a(x - h)^2 + k $, where:  
- $ (h, k) $ is the vertex.  
- $ a $ determines the width and direction of the parabola.  

**Example**: $ y = 2(x - 1)^2 + 3 $ has vertex at $ (1, 3) $, opens upwards, and $ a = 2 $ (wider than standard form).  

#### 3. Discriminant  
The discriminant $ \Delta = b^2 - 4ac $ determines the nature of roots:  
- $ \Delta > 0 $: Two distinct real roots.  
- $ \Delta = 0 $: One real root (double root).  
- $ \Delta < 0 $: No real roots (complex roots).  

**Example**: For $ x^2 - 4x + 3 = 0 $, $ \Delta = 16 > 0 $, so two real roots at $ x = 1 $ and $ x = 3 $.  

#### 4. Max-Min Problems  
To find max/min values:  
1. Use vertex form $ y = a(x - h)^2 + k $.  
2. If $ a > 0 $, the vertex is the minimum; if $ a < 0 $, it is the maximum.  

**Example**: Maximize $ y = -x^2 + 6x - 5 $. Vertex at $ x = 3 $, $ y = 6 $, so maximum value is 6.  

#### 5. Axis of Symmetry  
The axis of symmetry is $ x = \frac{-b}{2a} $. It divides the parabola into two mirror images.  

**Example**: For $ y = 2x^2 - 4x + 1 $, axis of symmetry is $ x = 1 $.  

---

### Examples  

#### 1. Basic Example  
**Problem**: Graph $ y = x^2 - 4x + 3 $ and find the vertex.  
**Solution**:  
- Vertex at $ x = \frac{-(-4)}{2(1)} = 2 $, $ y = (2)^2 - 4(2) + 3 = -1 $.  
- Graph: Parabola opening upward, vertex at $ (2, -1) $.  

#### 2. Applied Example  
**Problem**: A rectangular garden has a perimeter of 20 meters. Maximize the area.  
**Solution**:  
Let length = $ x $, width = $ \frac{20 - 2x}{2} = 10 - x $.  
Area = $ x(10 - x) = -x^2 + 10x $.  
Maximized at $ x = 5 $, area = 25 m².  

---

### Practice Problems  

#### 1. Find the vertex and axis of symmetry of $ y = 3x^2 - 12x + 5 $.  
**Answer**:  
- Vertex: $ x = \frac{-(-12)}{2(3)} = 2 $, $ y = 3(2)^2 - 12(2) + 5 = -1 $.  
- Axis of Symmetry: $ x = 2 $.  

#### 2. Solve $ 2x^2 - 5x - 3 = 0 $.  
**Answer**:  
Use quadratic formula:  
$$
x = \frac{5 \pm \sqrt{25 + 24}}{4} = \frac{5 \pm 7}{4}
$$  
Roots: $ x = 3 $, $ x = -\frac{1}{2} $.  

#### 3. Maximize the area of a rectangular garden with a fixed perimeter of 100 meters.  
**Answer**:  
Let length = $ x $, width = $ \frac{100 - 2x}{2} = 50 - x $.  
Area = $ x(50 - x) = -x^2 + 50x $.  
Maximized at $ x = 25 $, area = 3125 m².  

---

### Common Misunderstandings  

1. **Misapplying the Discriminant**:  
   - Students may confuse $ \Delta > 0 $ with two complex roots, but it actually indicates two real roots.  

2. **Confusing Vertex Form and Standard Form**:  
   - Vertex form $ y = a(x - h)^2 + k $ explicitly shows the vertex, while standard form $ y = ax^2 + bx + c $ requires solving for $ h $ to find the vertex.  

---

### References  
- **OpenStax Algebra and Calculus**: https://openstax.org/books/algebra-and-calculus-chapter-1-quadratic-functions  
- **CK-12 Algebra II**: https://www.ck12.org/alg2/section/2-4/lesson/2-4-vertex-form-of-a-quadratic-function/  

--- 

**Curriculum Coverage**  
- **Japan**: High School Mathematics Curriculum (Mathematics Curriculum Guidelines, 2023)  
- **UK**: A-Level Mathematics (Edexcel)  
- **IB**: IB Mathematics (Standard Level)  
- **Singapore**: National Curriculum (Mathematics Curriculum, 2022)  
- **US**: College Board AP Calculus AB/BC  
``` 

This module provides a structured approach to quadratic functions, emphasizing key concepts, examples, and problem-solving strategies while adhering to educational standards and referencing authoritative resources.