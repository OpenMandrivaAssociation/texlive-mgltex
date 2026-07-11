%global tl_name mgltex
%global tl_revision 63255

Name:		texlive-%{tl_name}
Epoch:		1
Version:	4.2
Release:	%{tl_revision}.1
Summary:	High-quality graphics from MGL scripts embedded in LaTeX documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/mgltex
License:	gpl3 cc-by-sa-3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mgltex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mgltex.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mgltex.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package allows you to create high-quality publication-ready
graphics directly from MGL scripts embedded into your LaTeX document,
using the MathGL library. Besides following the LaTeX philosophy of
allowing you to concentrate on content rather than output (mglTeX takes
care of producing the output), mglTeX facilitates the maintenance of
your document, since both code for text and code for plots are contained
in a single file. MathGL. is a fast and efficient library by Alexey
Balakin for the creation of high-quality publication-ready scientific
graphics. Although it defines interfaces for many programming languages,
it also implements its own scripting language, called MGL, which can be
used independently.

