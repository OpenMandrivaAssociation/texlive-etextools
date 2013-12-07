# revision 20694
# category Package
# catalog-ctan /macros/latex/contrib/etextools
# catalog-date 2010-12-08 18:13:15 +0100
# catalog-license lppl
# catalog-version 3.1415926
Name:		texlive-etextools
Version:	3.1415926
Release:	3
Summary:	e-TeX tools for LaTeX users and package writers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/etextools
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/etextools.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/etextools.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/etextools.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

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

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 3.1415926-2
+ Revision: 751597
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 3.1415926-1
+ Revision: 718377
- texlive-etextools
- texlive-etextools
- texlive-etextools
- texlive-etextools

