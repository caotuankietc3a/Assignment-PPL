# update: 16/07/2018
from dataclasses import dataclass
from abc import ABC
from AST import *


class Kind(ABC):
    pass


class Function(Kind):
    def __str__(self):
        return self.__class__.__name__


class Parameter(Kind):
    def __str__(self):
        return self.__class__.__name__


class Variable(Kind):
    def __str__(self):
        return self.__class__.__name__


class Identifier(Kind):
    def __str__(self):
        return self.__class__.__name__


class StaticError(Exception):
    pass


@dataclass
class Undeclared(StaticError):
    k: Kind
    n: str  # name of identifier

    def __str__(self):
        return "Undeclared " + str(self.k) + ": " + self.n


@dataclass
class Redeclared(StaticError):
    k: Kind
    n: str  # Name of Identifier

    def __str__(self):
        return "Redeclared " + str(self.k) + ": " + self.n


@dataclass
class Invalid(StaticError):
    k: Kind
    n: str  # name of identifier

    def __str__(self) -> str:
        return f"Invalid {str(self.k)}: {str(self.n)}"


@dataclass
class TypeMismatchInExpression(StaticError):
    exp: Expr

    def __str__(self):
        return "Type Mismatch In Expression: " + str(self.exp)


@dataclass
class TypeMismatchInStatement(StaticError):
    stmt: Stmt

    def __str__(self):
        return "Type Mismatch In Statement: " + str(self.stmt)


@dataclass
class MustInLoop(StaticError):
    stmt: Stmt

    def __str__(self):
        return f"Must In Loop: {str(self.stmt)}"


@dataclass
class IllegalArrayLiteral(StaticError):
    arr: ArrayLit

    def __str__(self):
        return "Illegal Array Literal: " + str(self.arr)


@dataclass
class InvalidStatementInFunction(StaticError):
    n: str  # name of function

    def __str__(self) -> str:
        return f"Invalid Statement In Function: {str(self.n)}"


class NoEntryPoint(StaticError):
    def __str__(self):
        return "No entry point"
