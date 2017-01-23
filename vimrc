" Copyright (c) 2015-2017 Joshua Gutow under the MIT License

" Vundle stuff
set nocompatible
filetype off
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

Plugin 'VundleVim/Vundle.vim'
Plugin 'bbchung/clighter8'
Plugin 'altercation/vim-colors-solarized'
Plugin 'JuliaEditorSupport/julia-vim'

call vundle#end()
filetype plugin indent on

" Sets how many lines of history VIM has to remember
set history=700

" Stops Vim from beeping
set noerrorbells visualbell t_vb=
if has('autocmd')
    autocmd GUIEnter * set visualbell t_vb=
endif

"Show current line number
set number

"Show a ruler
set colorcolumn=81
"Stop vim word word wrapping automatically
set textwidth=0

" Enable syntax highlighting
syntax enable

" Set solarized as the colorscheme
" set background=dark
colorscheme solarized
" TODO: Fix solarized  light toggle...
call togglebg#map("<F5>")

" 1 tab is 4 columns wide and uses \t
set shiftwidth=4
set tabstop=4
set softtabstop=4
set noexpandtab

" Automatically match the indent of the previous line
set autoindent

" Set fdm to syntax
set fdm=indent
" Open all folds
set foldlevel=99

" Setting for list view
set lcs=tab:\>\ ,trail:\-

" I want spellcheck
set spell

" change into dir when opening a file
" set autochdir TODO: different ways to do this that work better

" Auto indent in python/java
autocmd BufRead *.py set smartindent cinwords=:
autocmd BufRead *.py set expandtab tabstop=4 shiftwidth=4 softtabstop=4
autocmd BufRead *.hs set expandtab tabstop=8 shiftwidth=4 softtabstop=4 spell!
autocmd BufRead *.scm set expandtab tabstop=4 shiftwidth=4 softtabstop=4
autocmd BufRead *.java set smartindent cinwords={,)
" Automatically delete trailing whitespace
autocmd FileType c,cpp,java,scm,py autocmd BufWritePre <buffer> :%s/\s\+$//e

