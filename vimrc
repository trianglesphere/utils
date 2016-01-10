" Copyright (c) 2015 Joshua Gutow under the MIT License

" Sets how many lines of history VIM has to remember
set history=700

" Stops Vim from beeping
set noerrorbells visualbell t_vb=
if has('autocmd')
    autocmd GUIEnter * set visualbell t_vb=
endif

"Show current line number
set nu

"Show a ruler
set colorcolumn=80
"Stop vim word word wrapping automatically
set tw=0

" Enable syntax highlighting
syntax enable

" Set monokai as the colorscheme
colorscheme monokai

" Set the font to Inconsolata
set guifont=Inconsolata

" 1 tab is 8 columns wide and uses \t
set shiftwidth=8
set tabstop=8
set softtabstop=8
set noexpandtab

" Automatically match the indent of the previous line
set autoindent

" Set fdm to indent
set fdm=indent
" Open all folds
set foldlevelstart=99

" Setting for list view
set lcs=tab:\|\ 

" Auto indent in python/java
autocmd BufRead *.py set smartindent cinwords=:
autocmd BufRead *.py set expandtab tabstop=4 shiftwidth=4 softtabstop=4
autocmd BufRead *.java set smartindent cinwords={,)

