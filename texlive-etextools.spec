Name:		texlive-etextools
Version:	3.1415926
Release:	1
Summary:	e-TeX tools for LaTeX users and package writers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/etextools
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/etextools.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/etextools.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/etextools.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package provides many (purely expandable) tools for LaTeX:
- Extensive list management (csv lists, lists of single
tokens/characters, etoolbox lists): * purely expandable loops
(csvloop, forcsvloop, etc.) * conversion (csvtolist, etc.)) *
addition/deletion (csvadd, listdel, etc.) - Expansion and group
control: \expandnext, \ExpandAfterCmds, \AfterGroup... - Tests
on tokens, characters and control sequences (\iffirstchar,
\ifiscs, \ifdefcount, \@ifchar...) - Tests on strings
(\ifstrnum, \ifuppercase, \DeclareStringFilter...) - Purely
expandable macros with options (\FE@testopt, \FE@ifstar) or
modifiers (\FE@modifiers) - Some purely expandable numerics
(\interval, \locinterplin). The package is dependent on the
etex and the etoolbox packages.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/etextools/etextools.sty
%doc %{_texmfdistdir}/doc/latex/etextools/README
%doc %{_texmfdistdir}/doc/latex/etextools/etextools-examples.pdf
%doc %{_texmfdistdir}/doc/latex/etextools/etextools-examples.tex
%doc %{_texmfdistdir}/doc/latex/etextools/etextools.pdf
#- source
%doc %{_texmfdistdir}/source/latex/etextools/etextools.drv
%doc %{_texmfdistdir}/source/latex/etextools/etextools.dtx
%doc %{_texmfdistdir}/source/latex/etextools/etextools.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
