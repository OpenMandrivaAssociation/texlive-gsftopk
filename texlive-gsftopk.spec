%global tl_name gsftopk
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.19.2
Release:	%{tl_revision}.1
Summary:	Convert Ghostscript fonts to PK files
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/utilities/gsftopk
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gsftopk.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gsftopk.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(gsftopk.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Designed for use with xdvi and dvips this utility converts Adobe Type 1
fonts to PK bitmap format. It should not ordinarily be much used
nowadays, since both its target applications are now capable of dealing
with Type 1 fonts, direct.

