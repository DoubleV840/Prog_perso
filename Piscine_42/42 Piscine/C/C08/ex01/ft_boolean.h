/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_boolean.h                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: wberger <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/07/20 09:36:55 by wberger           #+#    #+#             */
/*   Updated: 2022/07/20 14:27:07 by wberger          ###   ########lyon.fr   */
/*                                                                            */
/* ************************************************************************** */
#ifndef	FT_BOOLEAN_H
# define FT_BOOLEAN_H

# include <unistd.h>

typedef	char	t_bool;
# define EVEN(nbr) nbr % 2 == 0
# define FALSE 1
# define TRUE 0
# define EVEN_MSG "I have an even number of arguments."
# define ODD_MSG "I have an odd number of arguments."
# define SUCCESS 0

#endif
