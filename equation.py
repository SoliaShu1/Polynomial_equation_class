import copy
import math


class Polynomial:
    """Class for Polynomial representation"""
    def __init__(self, lst):
        """Initialiaing list of coefficients"""
        self.lst = lst

    def __str__(self):
        """Method for representing"""
        return "{}(coeffs={})".format(self.__class__.__name__, self.lst)

    def degree(self):
        """Returns power of equation"""
        while self.lst[0] == 0:
            del self.lst[0]
        return len(self.lst) - 1

    def coeff(self, number):
        """Returns a coefficient"""
        return self.lst[len(self.lst) - 1 - number]

    def evalAt(self, value):
        """Evaluates equation with given value"""
        return sum([self.lst[i] * value **
                    (len(self.lst) - i - 1) for i in range(len(self.lst))])

    def __eq__(self, other):
        """Checks equality"""
        remain = list(copy.copy(self.lst))
        if len(self.lst) == 1:
            return self.lst[0] == other
        elif len(self.lst) == 0:
            return len(self.lst) == other.lst[0]
        elif len(self.lst) > 1:
            while remain[0] == 0:
                del remain[0]
            return remain == other.lst
        return len(self.lst) == len(other.lst)

    def __ne__(self, other):
        """Check inequality"""
        count = 0
        if isinstance(self, self.__class__) and \
                isinstance(other, self.__class__):
            if len(self.lst) != len(other.lst):
                return True
            elif len(self.lst) == len(other.lst):
                for i in range(len(self.lst)):
                    if self.lst[i] == other.lst[i]:
                        count += 1
                if count == len(self.lst):
                    return False
                else:
                    return True
        return True

    def __hash__(self):
        """Method for hashing"""
        return hash(self.lst[0])

    def scaled(self, number):
        """Multiplies each coefficient"""
        return self.__class__([i*number for i in self.lst])

    def derivative(self):
        """Derivative function"""
        return self.__class__([self.lst[i] * (len(self.lst) - i - 1)
                               for i in range(len(self.lst) - 1)])

    def addPolynomial(self, polym):
        """Adds polynomials"""
        j = 0
        work_with = copy.copy(self.lst)
        if isinstance(self, self.__class__) and \
                isinstance(polym, self.__class__):
            new = work_with[:(len(self.lst) - len(polym.lst))]
            del work_with[:(len(work_with) - len(polym.lst))]
            for i in range(len(work_with)):
                new.append(work_with[j] + polym.lst[j])
                j += 1
            return self.__class__(new)
        return None

    def multiplyPolynomial(self, polym):
        """Multiplies polynomials"""
        work_with = copy.copy(self.lst)
        prod = [0] * (len(self.lst) + len(polym.lst) - 1)

        try:
            for i in range(len(polym.lst)):
                for j in range(len(self.lst)):
                    prod[i + j] += work_with[i] * polym.lst[j]
        except IndexError:
            pass

        return self.__class__(prod)


class Quadratic(Polynomial):
    """Class for representing quadratic equation"""
    def __init__(self, lst):
        """Initializing coefficients"""
        super().__init__(lst)
        if len(self.lst) != 3:
            raise Exception

    def __str__(self):
        """Method for representing"""
        return "{}(a={}, b={}, c={})".format(
            self.__class__.__name__, self.lst[0], self.lst[1], self.lst[2])

    def discriminant(self):
        """Takes a discriminant"""
        return (self.lst[1] ** 2) - (4 * self.lst[0] * self.lst[2])

    def numberOfRealRoots(self):
        """Returns number of roots"""
        if self.discriminant() >= 1:
            return 2
        elif self.discriminant() == 0:
            return 1
        else:
            return 0

    def getRealRoots(self):
        """Returns list of roots"""
        return sorted(list(set([((-1 * self.lst[1]) +
                                 (i * math.sqrt(self.discriminant()))) / 2
                                * self.lst[0] for i in [-1, 1]]
                               if self.numberOfRealRoots() > 0 else list())))
