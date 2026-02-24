## An implementation of a Vector with variable dimensions

from collections.abc import Iterable
from math import sqrt, trunc, floor, ceil, nan

class Vector:
    """
    An implementation of a multi-dimensional Vector with support for math operator and functions.
    """

    # *----------------------*
    # *------- virtual ------*

    # access

    def __init__(self, *args : float | int | list[float | int] | tuple[int, float | int]) -> None: 
        """
        A simple implementation of a Vector class with variable amount of dimensions.
        
        :Constructors:

        • series of float or integer:
            `Vector(1.0, 2.0, 3.0)`, `Vector(1, 2, 3)`
        
        • list of float or list of integer:
            `Vector([1.0, 2.0, 3.0])`, `Vector([1, 2, 3])`

        • tuple of one int and a float or integer:
            `Vector((3, 1.0)) # returns a vector with values (1.0, 1.0, 1.0)`,
            `Vector((3, 1)) # returns a vector with values (1, 1, 1)`
        """
        
        self.d : list[float | int] = []
        if not len(args) > 0 : return 
        
        # series of numbers
        if all((type(arg) is float or type(arg) is int) for arg in args):
            for d in args: 
                self.d.append(d) # type: ignore

        # list of numbers
        elif type(args[0]) is list: 
            for d in args[0]:
                self.d.append(d)
        
        # tuple of dimensions and value
        elif type(args[0]) is tuple and len(args[0]) == 2 and type(args[0][0]) is int and (type(args[0][1]) is float or type(args[0][1]) is int):
            for _ in range(args[0][0]):
                self.d.append(args[0][1])
        

    # containers

    def __len__(self) -> int:
        return len(self.d)
    
    def __getitem__(self, index : int) -> float:
        return self.d[index]

    def __setitem__(self, index : int, data : float | int) -> None:
        self.d[index] = data

    def __contains__(self, item : float | int) -> bool:
        return item in self.d

    # conversions

    def __str__(self) -> str:
        output : str = ""
        if len(self.d) < 10:
            for d in self.d:
                output = output + str(d) + ", "
        else:
            for d in range(5):
                output = output + str(self.d[d]) + ", "
            output = output[:-2]
            output += " ... "
            for d in range(len(self.d)-6, len(self.d) - 1):
                output = output + str(self.d[d]) + ", "
        output = output[:-2]
        output = "(" + output + ")"
        return output
    
    def __neg__(self) -> Vector:
        ls : list[float | int] = []
        for i in self:
            ls.append(-i)
        return Vector(ls)

    def __pos__(self) -> Vector:
        return self

    def __abs__(self) -> Vector:
        ls : list[float | int] = []
        for i in self:
            ls.append(abs(i))
        return Vector(ls)

    def __invert__(self) -> Vector:
        ls : list[float | int] = []
        for i in self:
            ls.append(-i - 1)
        return Vector(ls)

    def __int__(self) -> Vector:
        ls : list[float | int] = []
        for i in self:
            ls.append(int(i))
        return Vector(ls)
    
    def __float__(self) -> Vector:
        ls : list[float | int] = []
        for i in self:
            ls.append(float(i))
        return Vector(ls)

    def __round__(self, ndigits : int = 1) -> Vector: 
        ls : list[float | int] = []
        for i in self:
            ls.append(round(i, ndigits))
        return Vector(ls)

    def __trunc__(self) -> Vector:
        ls : list[float | int] = []
        for i in self:
            ls.append(trunc(i))
        return Vector(ls)

    def __floor__(self) -> Vector:
        ls : list[float | int] = []
        for i in self:
            ls.append(floor(i))
        return Vector(ls)

    def __ceil__(self) -> Vector:
        ls : list[float | int] = []
        for i in self:
            ls.append(ceil(i))
        return Vector(ls)
    
    # math

    # simple member-member addition. assert error in unmatched lengths or invalid types
    def __add__(self, other : Vector | float) -> Vector: 
        assert (type(other) is Vector or type(other) is float or type(other) is int), f"Invalid type '{type(other)}' for addition operation with Vector."
        if type(other) is Vector:
            assert len(self) == len(other) , f"Non-matching Vector lengths." 
        ls : list[float | int] = []
        if type(other) is Vector:
            for i in range(len(self)):
                ls.append(self[i] + other[i]) 
        elif type(other) is float or type(other) is int:
            for i in self:
                ls.append(i + other) 
        return Vector(ls)

    # simple member-member subtraction. assert error in unmatched lengths or invalid types
    def __sub__(self, other : Vector | float) -> Vector: 
        assert (type(other) is Vector or type(other) is float or type(other) is int), f"Invalid type '{type(other)}' for subtraction operation with Vector."
        if type(other) is Vector:
            assert len(self) == len(other) , f"Non-matching Vector lengths." 
        ls : list[float | int] = []
        if type(other) is Vector:
            for i in range(len(self)):
                ls.append(self[i] - other[i]) 
        elif type(other) is float or type(other) is int:
            for i in self:
                ls.append(i - other) 
        return Vector(ls)

    # simple member-member multiplication. assert error in unmatched lengths or invalid types
    def __mul__(self, other : Vector | float) -> Vector: 
        assert (type(other) is Vector or type(other) is float or type(other) is int), f"Invalid type '{type(other)}' for multiplication operation with Vector."
        if type(other) is Vector:
            assert len(self) == len(other) , f"Non-matching Vector lengths." 
        ls : list[float | int] = []
        if type(other) is Vector:
            for i in range(len(self)):
                ls.append(self[i] * other[i]) 
        elif type(other) is float or type(other) is int:
            for i in self:
                ls.append(i * other) 
        return Vector(ls)
    
    # simple member-member division. assert error in unmatched lengths or invalid types
    def __truediv__(self, other : Vector | float) -> Vector: 
        assert (type(other) is Vector or type(other) is float or type(other) is int), f"Invalid type '{type(other)}' for division operation with Vector."
        if type(other) is Vector:
            assert len(self) == len(other) , f"Non-matching Vector lengths." 
        ls : list[float | int] = []
        if type(other) is Vector:
            for i in range(len(self)):
                ls.append(self[i] / other[i]) 
        elif type(other) is float or type(other) is int:
            for i in self:
                ls.append(i / other) 
        return Vector(ls)

    # each element is raised to the power
    def __pow__(self, power : float) -> Vector:
        assert (type(power) is float or type(power) is int), f"Invalid type '{type(power)}' for division operation with Vector."
        ls : list[float | int] = []
        for i in self:
            ls.append(pow(i, power))
        return Vector(ls)

    # simple member-member addition. assert error in unmatched lengths or invalid types
    def __iadd__(self, other : Vector | float) -> Vector: 
        self = self + other 
        return self 
    
    # simple member-member subtraction. assert error in unmatched lengths or invalid types
    def __isub__(self, other : Vector | float) -> Vector: 
        self = self - other 
        return self 

    # simple member-member multiplication. assert error in unmatched lengths or invalid types
    def __imul__(self, other : Vector | float) -> Vector: 
        self = self * other 
        return self 

    # simple member-member division. assert error in unmatched lengths or invalid types
    def __itruediv__(self, other : Vector | float) -> Vector:  
        self = self / other 
        return self 

    # each element is raised to the power
    def __ipow__(self, other : float) -> Vector:
        self = self ** other
        return self

    # comparisons

    # self < other
    def __lt__(self, other : Vector) -> bool:
        assert len(self) == len(other.d), f"{self} and {other} do not have the same length of members."
        for i in range(len(self)):
            if self[i] >= other[i]:
                return False
        return True

    # self <= other
    def __le__(self, other : Vector) -> bool:
        assert len(self) == len(other.d), f"{self} and {other} do not have the same length of members."
        for i in range(len(self)):
            if self[i] > other[i]:
                return False
        return True

    # self > other
    def __gt__(self, other : Vector) -> bool:
        return not (self <= other)

    # self >= other
    def __ge__(self, other : Vector) -> bool:
        return not (self < other)

    
    # *----------------------*
    # *------- public -------*


    # math

    
    # self operations

    # normalized vector. same direction with length 1
    def normalized(self) -> Vector:
        return self / self.norm()


    # euclidean norm calculated as sqrt( Σ(i**i) )
    def norm(self) -> float:
        res : float = 0.0
        for i in self:
            res += i*i
        return sqrt(res)
    
    
    # operations with other vectors

    # dot product calculated as Σ(v1.di*v2.di)
    def dot(self, other : Vector) -> float:
        assert len(self) == len(other), f"{self} and {other} do not have the same length."
        res : float = 0.0
        for i in range(len(self)):
            res += self[i] * other[i]
        return res


    # cosine
    def cos(self, other : Vector) -> float:
        assert len(self) == len(other), f"{self} and {other} do not have the same length."
        try:
            return (self.dot(other)) / (self.norm() * other.norm())
        except ZeroDivisionError:
            return 0.0


    # sine
    def sin(self, other : Vector) -> float:
        assert len(self) == len(other), f"{self} and {other} do not have the same length."
        return Vector.get_sin_from_cos(self.cos(other))


    # tangent
    def tan(self, other : Vector) -> float:
        assert len(self) == len(other), f"{self} and {other} do not have the same length."
        cos = self.cos(other)
        sin = Vector.get_sin_from_cos(cos)
        try:
            return sin / cos
        except ZeroDivisionError:
            return nan


    # secant
    def sec(self, other : Vector) -> float:
        assert len(self) == len(other), f"{self} and {other} do not have the same length."
        try:
            return 1.0 / self.cos(other)
        except ZeroDivisionError:
            return 0.0


    # cosecant
    def csc(self, other : Vector) -> float:
        assert len(self) == len(other), f"{self} and {other} do not have the same length."
        try:
            return 1.0 / self.sin(other)
        except:
            return 0.0


    # cotangent
    def cot(self, other : Vector) -> float:
        assert len(self) == len(other), f"{self} and {other} do not have the same length."
        cos = self.cos(other)
        sin = Vector.get_sin_from_cos(cos)
        try:
            return cos / sin
        except ZeroDivisionError:
            return nan
        
        
    # comparisons

    def eq_values(self, other : Vector) -> bool:
        """
        Check if all the values of this Vector are equal to the respective values of the other Vector.
        
        :param other: The Vector that's compared to this Vector.
        :type other: Vector
        :return: `True` if `self[i] == other[i]` `for i in len(range(self))`.
        :rtype: bool
        """
        assert len(self) == len(other), f"{self} and {other} do not have the same length."
        for i in range(len(self)):
            if self[i] != other[i]:
                return False
        return True


    # access

    def num_dimensions(self) -> int:
        return len(self)


    def front(self) -> float:
        return self.d[0]


    def back(self) -> float:
        return self.d[len(self) - 1]


    def get(self, index : int) -> (float | int):
        return self[index]


    def length(self) -> float:
        """
        Abbreviation of norm.
        
        :return: Returns the length of the Vector.
        :rtype: float
        """
        return self.norm()


    def print(self) -> None:
        print(str(self))

    
    # converters

    def copy(self) -> Vector:
        return Vector(self.d)


    def to_string(self) -> str:
        return str(self)
    

    def to_list(self) -> list[float | int]:
        return_ls : list[float | int] = []
        for d in self:
            return_ls.append(d)
        return return_ls

    
    # mutate

    def set_all(self, value: float | int) -> None:
        for i in range(len(self)):
            self[i] = value

    
    def append(self, n : float) -> None:
        self.d.append(n)

    
    def extend(self, iterable : Iterable[float | int] | Vector) -> None:
        extender : Iterable[float | int] = []
        if type(iterable) == Vector:
            extender = iterable.to_list()
        if type(iterable) == Iterable[float | int]:
            extender = iterable
        self.d.extend(extender)
    
    
    def insert(self, index : int, value : float) -> None:
        assert index < len(self.d), f"Index '{index}' out of range."
        self.d.insert(index, value)

    
    def remove(self, index : int) -> None:
        assert index < len(self.d), f"Index '{index}' out of range."
        self.d.remove(index)

    
    def pop(self, index : int) -> float:
        assert index < len(self.d), f"Index '{index}' out of range."
        return self.d.pop(index)

    
    def pop_front(self) -> float:
        return self.d.pop(0)

    
    def pop_back(self) -> float:
        return self.d.pop()

    
    def clear(self) -> None:
        self.d.clear()


    # *----------------------*
    # *------- static -------*

    @staticmethod
    def get_sin_from_cos(cos : float) -> float:
        return sqrt(1 - (cos ** 2))


# *****************************************************
