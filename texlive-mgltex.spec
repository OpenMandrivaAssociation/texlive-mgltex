Name:		texlive-mgltex
Version:	63255
Release:	1
Summary:	High-quality graphics from MGL scripts embedded in LaTeX documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mgltex
License:	gpl3 cc-by-sa-3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mgltex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mgltex.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mgltex.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package allows you to create high-quality
publication-ready graphics directly from MGL scripts embedded
into your LaTeX document, using the MathGL library. Besides
following the LaTeX philosophy of allowing you to concentrate
on content rather than output (mglTeX takes care of producing
the output), mglTeX facilitates the maintenance of your
document, since both code for text and code for plots are
contained in a single file. MathGL. is a fast and efficient
library by Alexey Balakin for the creation of high-quality
publication-ready scientific graphics. Although it defines
interfaces for many programming languages, it also implements
its own scripting language, called MGL, which can be used
independently.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/mgltex
%{_texmfdistdir}/tex/latex/mgltex
%doc %{_texmfdistdir}/doc/latex/mgltex

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
