# XML Schema:

It is a language which allows you to check legal format for xml document. 

## XSD:

A modern xml validator to check the format of the xml files.
XSD stands for XML Schema Driver. 

### Normal xml:

```
<person> 
<firstName> Name1 </firstName>
</person> 
```

### XSD structure:

This is xml schema contract. 
```
<xs:complexType name="person">
<xs:sequence>
  <xs:element name="firstName" type="xs:string;"/>
</xs:sequence>
</xs:complexType>
```
