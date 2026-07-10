%global tl_name etextools
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.1415926
Release:	%{tl_revision}.1
Summary:	e-TeX tools for LaTeX users and package writers
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/etextools
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/etextools.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/etextools.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/etextools.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides many (purely expandable) tools for LaTeX: Extensive
list management (csv lists, lists of single tokens/characters, etoolbox
lists); purely expandable loops (csvloop, forcsvloop, etc.); conversion
(csvtolist, etc.)); addition/deletion (csvadd, listdel, etc.); Expansion
and group control: \expandnext, \ExpandAfterCmds, \AfterGroup...; Tests
on tokens, characters and control sequences (\iffirstchar, \ifiscs,
\ifdefcount, \@ifchar...); Tests on strings (\ifstrnum, \ifuppercase,
\DeclareStringFilter...); Purely expandable macros with options
(\FE@testopt, \FE@ifstar) or modifiers (\FE@modifiers); Some purely
expandable numerics (\interval, \locinterplin). The package is dependent
on the etex and the etoolbox packages.

