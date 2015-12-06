# makefile for Java projects
# Copyright (c) 2015 Joshua Gutow under the MIT License

# Build specific info
BLDDIR	= build/
SRCDIR	= src/
NAME	= main


# Flags to compile with
JC	= javac
JFLAGS	= -d $(BLDDIR) -cp $(SRCDIR) -g -Xprefer:newer


# Does the compiling
$(NAME).class : $(SRCDIR)$(NAME).java

# Pattern matching for all compiling all java source files
%.class : %.java
	$(JC) $(JFLAGS) $<

# Adds the src directory to the search for .java files
vpath %.java $(SRCDIR)

# Cleans up the .class files and the subdirectories created
# If src/ contains other folders, this will not clean them up.
.PHONY : clean
clean:
	rm $(BLDDIR)*.class

